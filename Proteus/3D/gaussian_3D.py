"""
Gaussian pulse in 3D
"""
from __future__ import division
from past.utils import old_div
import numpy as np
from proteus import (Domain, Context, Gauges,
                     MeshTools as mt)
from proteus.Gauges import PointGauges, LineIntegralGauges, LineGauges
from proteus.Profiling import logEvent
from proteus.mprans.SpatialTools import Tank2D
from proteus.mprans import SpatialTools as st
import proteus.TwoPhaseFlow.TwoPhaseFlowProblem as TpFlow

# *************************** #
# ***** GENERAL OPTIONS ***** #
# *************************** #
opts= Context.Options([
    ("final_time",8.0,"Final time for simulation"),
    ("dt_output",0.1,"Time interval to output solution"),
    ("A",0.35,"amplitude"),
    ("sig2",4.0,"variance"),
    ("Lx",20,"Length of the domain in x"),
    ("Ly",0.3,"Length of the domain in y"),
    ("Lz",1.25,"Length of the domain in y"),
    ("bA", 0.0, "bathymetry A"),
    ("bB", 0.5, "bathymetry B"),
    ("slipOnBottom",False,"Slip Boundary condition on bottom?"),
    ("he",0.01,"Max mesh element diameter")])

# Navier-Stokes model
ns_model=1 #0: rans2p, 1: rans3p

# General parameters
final_time=opts.final_time
dt_output=opts.dt_output

# About the domain
Lx=opts.Lx
Ly=opts.Ly
Lz=opts.Lz
wx=2.0

# About the bathymetry
bA=opts.bA
bB=opts.bB

# About initial condition
mwl=0.55
A=opts.A
sig2=opts.sig2

# About boundaries
openTop=True
slipOnLeftAndRight=True
slipOnFrontAndBack=True

# ****************** #
# ***** GAUGES ***** #
# ****************** #
# None

# *************************** #
# ***** DOMAIN AND MESH ***** #
# ****************** #******* #
he = opts.he
boundaries=['left','right','bottom','top','front','back',]
boundaryTags=dict([(key,i+1) for (i,key) in enumerate(boundaries)])
bt = boundaryTags
vertices=[[0.,-Ly/2.,bA],        #0
          [Lx,-Ly/2.,bA],        #1
          [Lx,0.,bA],            #2
          [Lx,0.,bB],            #3
          [Lx,Ly/2.,bB],         #4
          [0.,Ly/2.,bB],         #5
          [0.,0.,bB],            #6
          [0.,0.,bA],            #7
          #
          [0.,-Ly/2.,Lz],    #8
          [wx,-Ly/2.,Lz],    #9
          [2*wx,-Ly/2.,1.0*Lz],    #10
          [Lx-2*wx,-Ly/2.,1.0*Lz], #11
          [Lx-wx,-Ly/2.,Lz], #12
          [Lx,-Ly/2.,Lz],    #13
          #
          [Lx,Ly/2.,Lz],     #14
          [Lx-wx,Ly/2.,Lz],  #15
          [Lx-2*wx,Ly/2.,1.0*Lz],  #16
          [2*wx,Ly/2.,1.0*Lz],     #17
          [wx,Ly/2.,Lz],     #18
          [0.,Ly/2.,Lz]]     #19
vertexFlags=[boundaryTags['bottom'], #0
             boundaryTags['bottom'], #1
             boundaryTags['bottom'], #2
             boundaryTags['bottom'], #3
             boundaryTags['bottom'], #4
             boundaryTags['bottom'], #5
             boundaryTags['bottom'], #6
             boundaryTags['bottom'], #7
             boundaryTags['top'],    #8
             boundaryTags['top'],    #9
             boundaryTags['top'],    #10
             boundaryTags['top'],    #11
             boundaryTags['top'],    #12
             boundaryTags['top'],    #13
             boundaryTags['top'],    #14
             boundaryTags['top'],    #15
             boundaryTags['top'],    #16
             boundaryTags['top'],    #17
             boundaryTags['top'],    #18
             boundaryTags['top']]    #19

facets=[[[0,1,2,7],[7,2,3,6],[6,3,4,5]], #bottom
        [[0,1,13,12,11,10,9,8]],         #front
        [[1,2,3,4,14,13]],               #right
        [[4,5,19,18,17,16,15,14]],       #back
        [[5,6,7,0,8,19]],                #left
        [[19,8,9,18]],   # top
        [[18,9,10,17]],  # top
        [[17,10,11,16]], # top
        [[15,16,11,12]], # top
        [[15,12,13,14]]] # top
#facets=[[[0,1,2,7],[7,2,3,6],[6,3,4,5]], #bottom
#        [[0,1,11,10,9,8]],         #front
#        [[1,2,3,4,12,11]],    #right
#        [[4,5,15,14,13,12]],       #back
#        [[5,6,7,0,8,15]],    #left
#        [[15,8,9,14],[14,9,10,13],[13,10,11,12]]]       #top
facetFlags=[boundaryTags['bottom'],
            boundaryTags['front'],
            boundaryTags['right'],
            boundaryTags['back'],
            boundaryTags['left'],
            boundaryTags['top'],
            boundaryTags['top'],
            boundaryTags['top'],
            boundaryTags['top'],
            boundaryTags['top']]
regions=[[0.5*wx,0.1*Ly,0.5*(Lz-max(bA,bB))+max(bA,bB)]]
regionFlags=[0]
domain = Domain.PiecewiseLinearComplexDomain(vertices=vertices,
                                             vertexFlags=vertexFlags,
                                             facets=facets,
                                             facetFlags=facetFlags,
                                             regions = regions,
                                             regionFlags = regionFlags)
domain.MeshOptions.setParallelPartitioningType('node')
domain.boundaryTags = boundaryTags
domain.writePoly("mesh")
domain.writePLY("mesh")
domain.writeAsymptote("mesh")
domain.MeshOptions.triangleOptions="VApq1.25q12feena%e" % ((he**3)/6.0,)

# ****************************** #
# ***** INITIAL CONDITIONS ***** #
# ****************************** #
class zero(object):
    def uOfXT(self,x,t):
        return 0.

class clsvof_init_cond(object):
    def uOfXT(self,X,t):
        x=X[0]
        y=X[1]
        z=X[2]
        eta = mwl + A*np.exp(-x**2/(2*sig2))
        return z-eta

# ******************************* #
# ***** BOUNDARY CONDITIONS ***** #
# ******************************* #
############
# VELOCITY #
############
# DIRICHLET #
def vel_u_DBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        return lambda x,t: 0.0 # this is zero for either slip or non-slip
    elif (flag==boundaryTags['front'] or flag==boundaryTags['back']):
        if slipOnFrontAndBack:
            return None
        else:
            return lambda x,t:  0.0
    elif flag==boundaryTags['bottom']:
        if opts.slipOnBottom:
            return None
        else:
            return lambda x,t: 0.0
    elif (flag==boundaryTags['top'] and openTop==False):
        return lambda x,t: 0.0
#
def vel_v_DBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        if slipOnLeftAndRight:
            return None
        else:
            return lambda x,t: 0.0
    elif (flag==boundaryTags['front'] or flag==boundaryTags['back']):
        return lambda x,t: 0.0 # this is zero for either slip or non-slip
    elif flag==boundaryTags['bottom']:
        if opts.slipOnBottom:
            return None
        else:
            return lambda x,t: 0.0
    elif (flag==boundaryTags['top'] and openTop==False):
        return lambda x,t: 0.0
#
def vel_w_DBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        if slipOnLeftAndRight:
            return None
        else:
            return lambda x,t: 0.0
    elif (flag==boundaryTags['front'] or flag==boundaryTags['back']):
        if slipOnFrontAndBack:
            return None
        else:
            return lambda x,t:  0.0
    elif flag==boundaryTags['bottom']:
        return lambda x,t: 0.0 # this is zero for either slip or non-slip
    elif (flag==boundaryTags['top'] and openTop==False):
        return lambda x,t: 0.0
#
# DIFFUSIVE FLUX #
def vel_u_DFBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        return None
    elif (flag==boundaryTags['front'] or flag==boundaryTags['back']):
        if slipOnFrontAndBack:
            return lambda x,t: 0.
        else:
            return None
    elif flag==boundaryTags['bottom']:
        if opts.slipOnBottom:
            return lambda x,t: 0
        else:
            return None
    elif flag==boundaryTags['top']:
        if openTop:
            return lambda x,t: 0.0
        else:
            return None
    else:
        return lambda x,t: 0.
#
def vel_v_DFBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        if slipOnLeftAndRight:
            return lambda x,t: 0.0
        else:
            return None
    elif (flag==boundaryTags['front'] or flag==boundaryTags['back']):
        return None
    elif flag==boundaryTags['bottom']:
        if opts.slipOnBottom:
            return lambda x,t: 0
        else:
            return None
    elif flag==boundaryTags['top']:
        if openTop:
            return lambda x,t: 0.0
        else:
            return None
    else:
        return lambda x,t: 0.
#
def vel_w_DFBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        if slipOnLeftAndRight:
            return lambda x,t: 0.0
        else:
            return None
    elif (flag==boundaryTags['front'] or flag==boundaryTags['back']):
        if slipOnFrontAndBack:
            return lambda x,t: 0.
        else:
            return None
    elif flag==boundaryTags['bottom']:
        return None
    elif flag==boundaryTags['top']:
        if openTop:
            return lambda x,t: 0.0
        else:
            return None
    else:
        return lambda x,t: 0.
#
######################
# PRESSURE INCREMENT #
######################
# DIRICHLET #
def pressure_increment_DBC(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 0.0
#
# ADVECTIVE FLUX #
def pressure_increment_AFBC(x,flag):
    if not (flag == boundaryTags['top'] and openTop):
        return lambda x,t: 0.0
#
# DIFUSSIVE FLUX #
def pressure_increment_DFBC(x,flag):
    if not (flag == boundaryTags['top'] and openTop):
        return lambda x,t: 0.0
#
############
# PRESSURE #
############
def pressure_DBC(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 0.0
#
def pressure_AFBC(x,flag):
    if not(flag == boundaryTags['top'] and openTop):
        return lambda x,t: 0.0
#
##########
# CLSVOF #
##########
def clsvof_DBC(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 1.0 # let only air in
#
def clsvof_AFBC(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return None
    else:
        return lambda x,t: 0.0
#
############################################
# ***** Create myTwoPhaseFlowProblem ***** #
############################################
outputStepping = TpFlow.OutputStepping(opts.final_time,dt_output=opts.dt_output)
initialConditions = {'pressure': zero(),
                     'pressure_increment': zero(),
                     'vel_u': zero(),
                     'vel_v': zero(),
                     'vel_w': zero(),
                     'clsvof': clsvof_init_cond()}
boundaryConditions = {
    # DIRICHLET BCs #
    'pressure_DBC': pressure_DBC,
    'pressure_increment_DBC':  pressure_increment_DBC,
    'vel_u_DBC': vel_u_DBC,
    'vel_v_DBC': vel_v_DBC,
    'vel_w_DBC': vel_w_DBC,
    'clsvof_DBC': clsvof_DBC,
    # ADVECTIVE FLUX BCs #
    'pressure_AFBC': pressure_AFBC,
    'pressure_increment_AFBC': pressure_increment_AFBC,
    'vel_u_AFBC': lambda x, flag: None,
    'vel_v_AFBC': lambda x, flag: None,
    'vel_w_AFBC': lambda x, flag: None,
    'clsvof_AFBC': clsvof_AFBC,
    # DIFFUSIVE FLUX BCs #
    'pressure_increment_DFBC': pressure_increment_DFBC,
    'vel_u_DFBC': vel_u_DFBC,
    'vel_v_DFBC': vel_v_DFBC,
    'vel_w_DFBC': vel_w_DFBC,
    'clsvof_DFBC': lambda x, flag: None}

myTpFlowProblem = TpFlow.TwoPhaseFlowProblem(ns_model=ns_model,
                                             nd=3,
                                             cfl=0.25,
                                             outputStepping=outputStepping,
                                             structured=False,
                                             he=he,
                                             nnx=None,
                                             nny=None,
                                             nnz=None,
                                             domain=domain,
                                             initialConditions=initialConditions,
                                             boundaryConditions=boundaryConditions,
                                             auxVariables=None,
                                             fastArchive=False)
myTpFlowProblem.physical_parameters['gravity'] = [0.0,0.0,-9.8]
myTpFlowProblem.clsvof_parameters['disc_ICs']=False
myTpFlowProblem.rans3p_parameters['ns_forceStrongDirichlet']=True
myTpFlowProblem.rans3p_parameters['ARTIFICIAL_VISCOSITY'] = 3 #based on smoothness indicator

# clsvof #
myTpFlowProblem.clsvof_parameters['lambdaFact'] = 10.0
