"""
Gaussian pulse in 2D
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
    # About time #
    ("final_time",10.0,"Final time for simulation"),
    ("dt_output",0.1,"Time interval to output solution"),
    # About the domain #
    ("Lx",20,"Length of the domain in x"),
    ("bA",0.5,"Location of the bathymetry"),
    # Initial condition #
    ("mwl",0.75,"mean water level"),
    ("A",0.05,"amplitude"),
    ("sig2",2.0,"variance"),
    # About the mesh #
    ("he",0.01,"level of refinement"),
    ("structured",True,"Use structured mesh")],)

# Navier-Stokes model
ns_model=1 #0: rans2p, 1: rans3p

# General parameters
final_time=opts.final_time
dt_output=opts.dt_output

# About the domain
Lx=opts.Lx

# About bathymetry
bA=bB=opts.bA

# About initial condition
mwl  = opts.mwl
A    = opts.A
sig2 = opts.sig2

# about boundaries
openTop=True
slipOnLeftAndRight=True

# ****************** #
# ***** GAUGES ***** #
# ****************** #
# None

# *************************** #
# ***** DOMAIN AND MESH ***** #
# *************************** #
boundaries=['bottom','right','top','left']
boundaryTags=dict([(key,i+1) for (i,key) in enumerate(boundaries)])
if opts.structured:
    domain = Domain.RectangularDomain(L=(Lx,1.0-bA),x=[0.,bA,0.])
    nnx = np.int(Lx*np.int(1.0/opts.he))+1
    nny = np.int((1.-bA)*(1.0/opts.he))+1
else:
    nnx=nny=None
    vertices=[[0.0,bA],#0
              [Lx,bA], #1
              [Lx,1.0], #2
              [0.0,1.0]]#5
    vertexFlags=[boundaryTags['bottom'],
                 boundaryTags['bottom'],
                 boundaryTags['top'],
                 boundaryTags['top']]
    segments=[[0,1],
              [1,2],
              [2,3],
              [3,0]]
    segmentFlags=[boundaryTags['bottom'],
                  boundaryTags['right'],
                  boundaryTags['top'],
                  boundaryTags['left']]
    regions=[[0.1, 0.1]]
    regionFlags=[1]
    domain = Domain.PlanarStraightLineGraphDomain(vertices=vertices,
                                                  vertexFlags=vertexFlags,
                                                  segments=segments,
                                                  segmentFlags=segmentFlags,
                                                  regions = regions,
                                                  regionFlags = regionFlags)
    domain.writePoly("mesh")
    domain.writePLY("mesh")
    domain.writeAsymptote("mesh")
    triangleOptions = "VApq30Dena%8.8f" % ((opts.he**2)/2.0,)
    domain.MeshOptions.triangleOptions = triangleOptions
#
# boundary tags
domain.MeshOptions.setParallelPartitioningType('node')
domain.boundaryTags = boundaryTags

# ****************************** #
# ***** INITIAL CONDITIONS ***** #
# ****************************** #
class zero():
    def uOfXT(self,x,t):
        return 0.

class clsvof_init_cond():
    def uOfXT(self,X,t):
        x=X[0]
        y=X[1]
        eta = mwl + A*np.exp(-x**2/(2*sig2))
        return y-eta

class vel_x_init_cond(object):
    def uOfXT(self,X,t):
        return 0.0

class vel_y_init_cond(object):
    def uOfXT(self,X,t):
        return 0.0

# ******************************* #
# ***** BOUNDARY CONDITIONS ***** #
# ******************************* #
# Bottom: non-slip.
# Top: either open or non-slip. See openTop
# Left and right: either non-slip or slip. See slipOnLeftAndRight
############
# VELOCITY #
############
checkBoundaryTags=False
# DIRICHLET #
def vel_u_DBC(x,flag):
    if checkBoundaryTags:
        if flag==boundaryTags['left']:
            assert x[0]==0, "problem at left boundary"
        if flag==boundaryTags['right']:
            assert x[0]==Lx, "problem at right boundary"
        if flag==boundaryTags['bottom']:
            assert x[1]==0.5, "problem at bottom boundary"
        if flag==boundaryTags['top']:
            assert x[1]==1.0, "problem at top boundary"        
    #
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        return lambda x,t: 0.0 # this is zero for either slip or non-slip
    elif flag==boundaryTags['bottom']:
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
    elif flag==boundaryTags['bottom']:
        return lambda x,t: 0.0
    elif (flag==boundaryTags['top'] and openTop==False):
        return lambda x,t: 0.0
#
# DIFFUSIVE FLUX #
def vel_u_DFBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
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
def vel_v_DFBC(x,flag):
    if (flag==boundaryTags['left'] or flag==boundaryTags['right']):
        if slipOnLeftAndRight:
            return lambda x,t: 0.0
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
outputStepping = TpFlow.OutputStepping(final_time,dt_output=dt_output)
initialConditions = {'pressure': zero(),
                     'pressure_increment': zero(),
                     'vel_u': vel_x_init_cond(),
                     'vel_v': vel_y_init_cond(),
                     'clsvof': clsvof_init_cond()}
boundaryConditions = {
    # DIRICHLET BCs #
    'pressure_DBC': pressure_DBC, 
    'pressure_increment_DBC': pressure_increment_DBC, 
    'vel_u_DBC': vel_u_DBC,
    'vel_v_DBC': vel_v_DBC,
    'clsvof_DBC': clsvof_DBC, 
    # ADVECTIVE FLUX BCs #
    'pressure_AFBC': pressure_AFBC, 
    'pressure_increment_AFBC': pressure_increment_AFBC, 
    'vel_u_AFBC': lambda x, flag: None,
    'vel_v_AFBC': lambda x, flag: None,
    'clsvof_AFBC': clsvof_AFBC, 
    # DIFFUSIVE FLUX BCs #
    'pressure_increment_DFBC': pressure_increment_DFBC, 
    'vel_u_DFBC': vel_u_DFBC,
    'vel_v_DFBC': vel_v_DFBC,
    'clsvof_DFBC': lambda x, flag: None}
myTpFlowProblem = TpFlow.TwoPhaseFlowProblem(ns_model=ns_model,
                                             nd=2,
                                             cfl=0.25,
                                             outputStepping=outputStepping,
                                             structured=opts.structured,
                                             he=opts.he,
                                             nnx=nnx,
                                             nny=nny,
                                             nnz=1,
                                             domain=domain,
                                             initialConditions=initialConditions,
                                             boundaryConditions=boundaryConditions)
# physical parameters #
myTpFlowProblem.physical_parameters['gravity']=[0.0,-9.8,0.0]
# numerical parameters #
myTpFlowProblem.clsvof_parameters['disc_ICs']=False
myTpFlowProblem.rans3p_parameters['ns_forceStrongDirichlet']=True
myTpFlowProblem.rans3p_parameters['ARTIFICIAL_VISCOSITY']=3 #based on smoothness indicator
