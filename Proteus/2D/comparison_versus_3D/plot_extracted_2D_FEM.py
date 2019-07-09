import numpy as np
import matplotlib.pyplot as pl
from numpy import genfromtxt
from scipy.interpolate import interp2d
import numpy as np
from scipy.interpolate import griddata
from clawpack.petclaw.solution import Solution

def get_FEM_data_frame(name,path='FEM_DATA/'):
    # read data
    data = genfromtxt(path + '/' + name + '.csv', delimiter=',',skip_header=1)
    phi = data[:,1]
    x = data[:,7]
    y = data[:,8]
    
    # target grid to interpolate to
    Ny=1000
    Nx=8*Ny
    xi = np.linspace(x.min(),x.max(),Nx)
    yi = np.linspace(y.min(),y.max(),Ny)
    [yy,xx] = np.meshgrid(yi,xi)
    pphi = griddata((x,y),phi,(xx,yy),method='linear')
    
    return (xx,yy,pphi)
#
def plot_FEM_frame(x,y,phi,frame,fig,title=''):
    ax = fig.add_subplot(111)
    ax.set_aspect(aspect=1)
    pl.contour(x,y,phi,[0])
    pl.ylim([0.5, 1.0])
    pl.xlim([0., 4.0])
    pl.savefig('FEM_t'+frame+'.png')
    pl.close(fig)    
#

# ******************************* #
# ********** MAIN CODE ********** #
# ******************************* #

if True:
    #################
    # var=4, bA=0.5 #
    #################
    FEM_frame='var4_bA0p50'
    (xFEM,yFEM,phi) = get_FEM_data_frame(FEM_frame)
    fig = pl.figure(figsize=(16,12))
    ax = fig.add_subplot(111)
    ax.set_aspect(aspect=1)
    pl.contour(xFEM,yFEM-0.5,phi,[0],linewidths=3.5)
    pl.ylim([0.5, 0.9])
    pl.xlim([10., 15.0])
    pl.yticks([0.0,0.5,0.9])
    pl.gca().tick_params(axis="y", labelsize=25)
    pl.gca().tick_params(axis="x", labelsize=25)
    pl.savefig('var4_bA0p5.png',bbox_inches="tight")
    pl.close(fig)
    
    #################
    # var=4, bA=0.0 #
    #################
    FEM_frame='var4_bA0p00'
    (xFEM,yFEM,phi) = get_FEM_data_frame(FEM_frame)
    fig = pl.figure(figsize=(16,12))
    ax = fig.add_subplot(111)
    ax.set_aspect(aspect=1)
    pl.contour(xFEM,yFEM,phi,[0],linewidths=3.5)
    pl.ylim([0.0, 0.9])
    pl.xlim([15., 20.0])
    pl.yticks([0.0,0.5,0.9])
    pl.gca().tick_params(axis="y", labelsize=25)
    pl.gca().tick_params(axis="x", labelsize=25)
    pl.savefig('var4_bA0p0.png',bbox_inches="tight")
    pl.close(fig)
#

if False:
    #################
    # var=4, bA=0.5 #
    #################
    for t in [0,1,2,3,4,5,6,7]:
        FEM_frame='var4_bA0p5_t'+str(t)+'0'
        (xFEM,yFEM,phi) = get_FEM_data_frame(FEM_frame)
        fig = pl.figure(figsize=(16,8))
        ax = fig.add_subplot(111)
        ax.set_aspect(aspect=1)
        pl.contour(xFEM,yFEM-0.5,phi,[0],linewidths=3.5)
        pl.ylim([0.5, 0.9])
        pl.xlim([0.+1.5*t, 5.0+1.5*t])
        pl.yticks([0.0,0.25,0.5,0.75,0.9])
        pl.gca().tick_params(axis="y", labelsize=25)
        pl.gca().tick_params(axis="x", labelsize=25)
        pl.savefig('var4_bA0p5_t'+str(t)+'.png',bbox_inches="tight")
        pl.close(fig)

