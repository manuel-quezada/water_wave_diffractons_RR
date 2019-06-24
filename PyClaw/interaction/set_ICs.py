import numpy as np
from matplotlib import pyplot as pl
from clawpack.petclaw.solution import Solution
from clawpack.petclaw.fileio.petsc import write
import os

def bathymetry(x,y,bA=0.,bB=0.5):
    deltax=1000
    deltay=1.0
    alphax=0.5
    alphay=0.5
    aux = np.empty((1,len(x),len(y)), order='F')
    # xfrac and yfrac are x and y relative to deltax and deltay resp.
    xfrac=x-np.floor(x/deltax)*deltax
    yfrac=y-np.floor(y/deltay)*deltay
    # create a meshgrid out of xfrac and yfrac
    [yyfrac,xxfrac]=np.meshgrid(yfrac,xfrac)
    # bathymetry
    aux[0,:,:] = (bA*(xxfrac<=alphax*deltax)*(yyfrac<=alphay*deltay) +
                  bA*(xxfrac >alphax*deltax)*(yyfrac >alphay*deltay) +
                  bB*(xxfrac >alphax*deltax)*(yyfrac<=alphay*deltay) +
                  bB*(xxfrac<=alphax*deltax)*(yyfrac >alphay*deltay))
    [yy,xx]=np.meshgrid(y,x)
    aux[0,:,:] = aux[0,:,:]
    return  aux
#

# ************************************** #
# ********** READ DIFFRACTONS ********** #
# ************************************** #
path='./_output/isolated_waves/'
diff2=Solution(340,file_format='petsc',read_aux=False,path=path,file_prefix='wave2')
b2=bathymetry(diff2.state.grid.x.centers,diff2.state.grid.y.centers)
diff1=Solution(365,file_format='petsc',read_aux=False,path=path,file_prefix='wave1')
b1=bathymetry(diff1.state.grid.x.centers,diff1.state.grid.y.centers)

mwl=0.75
# compute water surface
eta1=diff1.state.q[0,:,:] + b1
eta2=diff2.state.q[0,:,:] + b2

# CO-PROPAGATING IC #
sol_co_propagating=Solution(340,file_format='petsc',read_aux=False,path=path,file_prefix='wave2')
sol_co_propagating.state.q[0,:,:] = (eta1-mwl)+(eta2-mwl)+mwl-b1
sol_co_propagating.state.q[1,:,:] = diff1.state.q[1,:,:] + diff2.state.q[1,:,:]
sol_co_propagating.state.q[2,:,:] = diff1.state.q[2,:,:] + diff2.state.q[2,:,:]
sol_co_propagating.state.t=0
if not os.path.exists('./_output/co-propagating'): os.mkdir('./_output/co-propagating')
write(sol_co_propagating,0,'./_output/co-propagating/')

# WRITE COUNTER-PROPAGATING INITIAL CONDITIONS #
sol_counter_propagating=Solution(340,file_format='petsc',read_aux=False,path=path,file_prefix='wave2')
sol_counter_propagating.state.q[0,:,:] = (eta1-mwl)+(eta2-mwl)+mwl-b2
sol_counter_propagating.state.q[1,:,:] = diff1.state.q[1,:,:] - diff2.state.q[1,:,:]
sol_counter_propagating.state.q[2,:,:] = diff1.state.q[2,:,:] - diff2.state.q[2,:,:]
sol_counter_propagating.state.t=0
if not os.path.exists('./_output/counter-propagating'): os.mkdir('./_output/counter-propagating')
write(sol_counter_propagating,0,'./_output/counter-propagating/')

# WRITE REFERENCE ICs #
sol_ref=Solution(340,file_format='petsc',read_aux=False,path=path,file_prefix='wave2')
sol_ref.state.q[0,:,:] = eta1-b1
sol_ref.state.q[1,:,:] = diff1.state.q[1,:,:]
sol_ref.state.q[2,:,:] = diff1.state.q[2,:,:]
sol_ref.state.t=0
if not os.path.exists('./_output/reference'): os.mkdir('./_output/reference')
write(sol_ref,0,'./_output/reference/')


