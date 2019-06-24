"""
Multiphase Flow Test
"""
from __future__ import division
from past.utils import old_div
import numpy as np
from proteus import (Domain, Context, Gauges,
                     MeshTools as mt)
from proteus.Gauges import PointGauges, LineIntegralGauges, LineGauges
from proteus.Profiling import logEvent
import proteus.TwoPhaseFlow.TwoPhaseFlowProblem as TpFlow
import math

# *************************** #
# ***** GENERAL OPTIONS ***** #
# *************************** #
opts= Context.Options([
    ("final_time",5.0,"Final time for simulation"),
    ("dt_output",0.1,"Time interval to output solution"),
    ("he",0.1,"Max mesh element diameter"),
    ("Lx",10.0,"Length of the domain in x")])

# Navier-Stokes model
ns_model=1 #0: rans2p, 1: rans3p

# about the domain
Lx=opts.Lx
Ly=1.0
Lz=1.0

# About bathymetry
bA=0.0
bB=0.5

# About initial condition 
mwl=0.55
A=0.35
sig2=0.1

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

bMax=0.5
Lx=5.0
Ly=1.0
Lz=1.0
vertices=[[0.,-0.05,0.0], #0
          [Lx,-0.05,0.0], #1
          [Lx,0.05,0.0],  #2
          [0.,0.05,0.0],  #3
          [0.,-Ly/2.,bMax], #4
          [Lx,-Ly/2.,bMax], #5
          [Lx,Ly/2.,bMax], #6
          [0.,Ly/2.,bMax], #7
          [0.,-Ly/2.,Lz], #8
          [Lx,-Ly/2.,Lz], #9
          [Lx,Ly/2.,Lz], #10
          [0,Ly/2.,Lz]] #11
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
             boundaryTags['top']]    #11
facets=[[[0,4,5,1]], #bottom
        [[0,1,2,3]], #bottom
        [[3,2,6,7]], #bottom
        [[4,5,9,8]], #front
        [[1,2,6,5]], #right
        [[5,6,10,9]], #right
        [[11,10,6,7]], #back
        [[0,4,7,3]], #left
        [[4,8,11,7]], #left
        [[11,8,9,10]]] #top
facetFlags=[boundaryTags['bottom'],
            boundaryTags['bottom'],
            boundaryTags['bottom'],
            boundaryTags['front'],
            boundaryTags['right'],
            boundaryTags['right'],
            boundaryTags['back'],
            boundaryTags['left'],
            boundaryTags['left'],
            boundaryTags['top']]
regions=[[0.5*Lx,0.0,0.5*Lz]]
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
        eta = mwl + A*np.exp(-(x-2)**2/(2*sig2))
        return z-eta
        
# ******************************* #
# ***** BOUNDARY CONDITIONS ***** #
# ******************************* #
non_slip_BCs=True
openTop=True
# DIRICHLET BOUNDARY CONDITIONS #
def vel_u_DBC(x,flag):
    # if non_slip_BCs and (flag == boundaryTags['box_left'] or
    #                      flag == boundaryTags['box_right'] or
    #                      flag == boundaryTags['box_top'] or
    #                      flag == boundaryTags['box_front'] or
    #                      flag == boundaryTags['box_back']):
    return lambda  x,t: 0.0

def vel_v_DBC(x,flag):
    # if non_slip_BCs and (flag == boundaryTags['box_left'] or
    #                      flag == boundaryTags['box_right'] or
    #                      flag == boundaryTags['box_top'] or
    #                      flag == boundaryTags['box_front'] or
    #                      flag == boundaryTags['box_back']):
    return lambda  x,t: 0.0

def vel_w_DBC(x,flag):
    # if non_slip_BCs and (flag == boundaryTags['box_left'] or
    #                      flag == boundaryTags['box_right'] or
    #                      flag == boundaryTags['box_top'] or
    #                      flag == boundaryTags['box_front'] or
    #                      flag == boundaryTags['box_back']):
    return lambda  x,t: 0.0
    
def pressure_increment_DBC(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 0.0    

def pressure_DBC(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 0.0

def clsvof_DBC(x,flag):
    if openTop and flag == boundaryTags['top']:
        return lambda x,t: 1.0
    
# ADVECTIVE FLUX BOUNDARY CONDITIONS #
def vel_u_AFBC(x,flag):
    # if non_slip_BCs and (flag == boundaryTags['box_left'] or
    #                      flag == boundaryTags['box_right'] or
    #                      flag == boundaryTags['box_top'] or
    #                      flag == boundaryTags['box_front'] or
    #                      flag == boundaryTags['box_back']):
    return None
    #elif openTop and flag == boundaryTags['top']:
    #    return None
    #else: #slip everywhere but the box
    #    return lambda x,t: 0.0

def vel_v_AFBC(x,flag):
    # if non_slip_BCs and (flag == boundaryTags['box_left'] or
    #                      flag == boundaryTags['box_right'] or
    #                      flag == boundaryTags['box_top'] or
    #                      flag == boundaryTags['box_front'] or
    #                      flag == boundaryTags['box_back']):
    return None
#elif openTop and flag == boundaryTags['top']:
#        return None
#    else: #slip everywhere but the box
#        return lambda x,t: 0.0

def vel_w_AFBC(x,flag):
#    if non_slip_BCs and (flag == boundaryTags['box_left'] or
#                         flag == boundaryTags['box_right'] or
#                         flag == boundaryTags['box_top'] or
#                         flag == boundaryTags['box_front'] or
#                         flag == boundaryTags['box_back']):
    return None
    #elif openTop and flag == boundaryTags['top']:
    #    return None
    #else: #slip everywhere but the box
    #    return lambda x,t: 0.0

def pressure_increment_AFBC(x,flag):
    if not (flag == boundaryTags['top'] and openTop):
        return lambda x,t: 0.0

def pressure_AFBC(x,flag):
    if not(flag == boundaryTags['top'] and openTop):
        return lambda x,t: 0.0
    
def clsvof_AFBC(x,flag):
    if openTop and flag == boundaryTags['top']:
        return None
    else:
        return lambda x,t: 0.0

# DIFFUSIVE FLUX BCs #
def pressure_increment_DFBC(x,flag):
    if not (flag == boundaryTags['top'] and openTop):
        return lambda x,t: 0.0
    
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
    'vel_u_AFBC': vel_u_AFBC,
    'vel_v_AFBC': vel_v_AFBC,
    'vel_w_AFBC': vel_w_AFBC,
    'clsvof_AFBC': clsvof_AFBC,
    # DIFFUSIVE FLUX BCs #
    'pressure_increment_DFBC': pressure_increment_DFBC,
    'vel_u_DFBC': lambda x, flag: lambda x,t: 0.,
    'vel_v_DFBC': lambda x, flag: lambda x,t: 0.,
    'vel_w_DFBC': lambda x, flag: lambda x,t: 0.,
    'clsvof_DFBC': lambda x, flag: None}

myTpFlowProblem = TpFlow.TwoPhaseFlowProblem(ns_model=ns_model,
                                             nd=3,
                                             cfl=0.2,
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
                                             useSuperlu=False)
myTpFlowProblem.physical_parameters['gravity'] = [0.0,0.0,-9.8]
myTpFlowProblem.clsvof_parameters['disc_ICs']=False
myTpFlowProblem.rans3p_parameters['ARTIFICIAL_VISCOSITY']=3 #based on smoothness indicator
