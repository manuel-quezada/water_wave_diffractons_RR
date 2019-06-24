import numpy as np
from matplotlib import pyplot as pl
from scipy.interpolate import interp2d
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

def get_FEM_data_frame(name,path,Lx):
    # read data
    print '... reading FEM data'
    data = np.genfromtxt(path + '/' + name + '.csv', delimiter=',',skip_header=1)
    phi = data[:,1]
    x = data[:,7]
    y = data[:,8]
    Ny=5
    Nx=Lx*Ny
    
    # target grid to interpolate to
    xi = np.linspace(x.min(),x.max(),Nx)
    yi = np.linspace(y.min(),y.max(),Ny)
    [yy,xx] = np.meshgrid(yi,xi)
    print '... interpolate FEM data'
    pphi = griddata((x,y),phi,(xx,yy),method='linear')    
    return (xx,yy,pphi)
#
def plot_FEM_contour_frame(x,y,phi,frame,title=''):
    pl.contour(x,y,phi,[0],
               colors=('r',),
               linewidths=(1,))
    pl.ylim([0.5, 1.0])
    pl.xlim([0., 100.0])
#
def plot_FEM_contour(name,Lx,marker='.r',shift=0):
    data = np.genfromtxt(name, delimiter=',',skip_header=1)
    c = data[:,7]
    xc= data[:,6]
    pl.plot(xc,c+shift,marker)
    if Lx==60:
        xextra = np.linspace(60,100,int(len(xc)/6.*4))
        pl.plot(xextra,0.75+xextra*0+shift,marker)
#

xlim=[0,100]
ylim=[0.74,0.7925]
#for time in [5,10,20,30]:
for time in [30]:
    print 'plotting time='+str(time)
    # ********************************* #
    # ********** DEEP DOMAIN ********** #
    # ********************************* #
    fig = pl.figure(figsize=(15,5))
    ax = fig.add_subplot(111)

    # SPECTRAL SOLUTION #
    mwl=0.75
    xKdV = np.genfromtxt('data_spectral/xKdV_deep.csv',delimiter=',')
    uKdV_deep = np.genfromtxt('data_spectral/uKdV_deep.csv',delimiter=',')
    pl.plot(xKdV,uKdV_deep[2*time]+mwl,'-g',linewidth=3)
    pl.xlim(xlim)    
    pl.ylim([0.74,0.79])
    ax.tick_params(labelsize=30)
    pl.savefig('KdV_deepBathymetry_t'+str(time),bbox_inches="tight")

    # FEM SOLUTION #
    fem_time = '0'+str(time) if time < 10 else str(time)
    plot_FEM_contour('data_FEM/nsDeep_contour_t'+fem_time+'0.csv',100,shift=0)
    pl.plot(xKdV,uKdV_deep[2*time]+mwl,'-g',linewidth=3)
    pl.savefig('KdV_vs_NS_deepBathymetry_t'+str(time),bbox_inches="tight")
    
    # ************************************ #
    # ********** SHALLOW DOMAIN ********** #
    # ************************************ #
    pl.clf()
    ax = fig.add_subplot(111)
    
    # SPECTRAL SOLUTION #
    mwl=0.25
    xKdV = np.genfromtxt('data_spectral/xKdV_shallow.csv',delimiter=',')
    uKdV_shallow = np.genfromtxt('data_spectral/uKdV_shallow.csv',delimiter=',')
    pl.plot(xKdV,uKdV_shallow[2*time]+mwl,'-g',linewidth=3)
    pl.xlim(xlim)
    pl.ylim([0.74-0.5,0.79-0.5])
    ax.tick_params(labelsize=30)
    pl.savefig('KdV_shallowBathymetry_t'+str(time),bbox_inches="tight")

    # FEM SOLUTION #
    plot_FEM_contour('data_FEM/nsShallow_contour_t'+fem_time+'0.csv',60,shift=-0.5)
    pl.plot(xKdV,uKdV_shallow[2*time]+mwl,'-g',linewidth=3)
    pl.savefig('KdV_vs_NS_shallowBathymetry_t'+str(time),bbox_inches="tight")
    
    # ************************************ #
    # ********** MEAN VALUE DOMAIN ********** #
    # ************************************ #
    pl.clf()
    ax = fig.add_subplot(111)
    # SPECTRAL SOLUTION #
    mwl=0.0
    xKdV = np.genfromtxt('data_spectral/xKdV_mean.csv',delimiter=',')
    uKdV_shallow = np.genfromtxt('data_spectral/uKdV_mean.csv',delimiter=',')
    pl.plot(xKdV,uKdV_shallow[2*time]+mwl,'-g',linewidth=3)
    pl.xlim(xlim)
    pl.ylim([0.74-0.25,0.79-0.25])
    ax.tick_params(labelsize=30)
    #pl.title('KdV and 2D-NS over shallow flat bathymetry at t='+str(time))
    pl.savefig('KdV_meanBathymetry_t'+str(time),bbox_inches="tight")
    
    # ************************************* #
    # ********** FV SIMULATION ************ #
    # ************************************* #
    pl.clf()
    ax = fig.add_subplot(111)
    
    x_FV = np.genfromtxt('data_FV/X_FV.csv',delimiter=',')[0]
    eta1_FV = np.genfromtxt('data_FV/eta1_FV.csv',delimiter=',')[2*time]
    eta2_FV = np.genfromtxt('data_FV/eta2_FV.csv',delimiter=',')[2*time]
    pl.plot(x_FV,eta1_FV,'-r',linewidth=3)
    pl.plot(x_FV,eta2_FV,'--b',linewidth=3)
    pl.xlim(xlim)
    pl.ylim(ylim)
    ax.tick_params(labelsize=30)
        
    pl.savefig('KdV_SWEs_t'+str(time)+'.png',bbox_inches="tight")
#
