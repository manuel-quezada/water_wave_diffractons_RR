import numpy as np
from matplotlib import pyplot as pl
from clawpack.petclaw.solution import Solution
from scipy.optimize import curve_fit

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

def fun(x,a,b):
    sech2 = 1.0/np.cosh(b*x)**2
    return a*sech2
#

def plot_waves(frame,path,num_waves):
    mwl=0.75
    all_waves_norm_h=[]
    all_waves_norm_x=[]
    lines=[]
    pl.clf()
    pl.figure(figsize=(15,10))

    colors=['blue','red','green','orange']

    # ***************************************** #
    # ********** PLOT ORIGINAL WAVES ********** #
    # ***************************************** #
    pl.clf()
    for wave in np.arange(1,num_waves+1):
        sol=Solution(frame,file_format='petsc',read_aux=False,path=path,file_prefix='wave'+str(wave))
        h=sol.state.q[0,:,:]
        hu=sol.state.q[1,:,:]
        x=sol.state.grid.x.centers
        y=sol.state.grid.y.centers
        my=len(y)
        mx=len(x)
        b=bathymetry(x,y)[0,:,:]
        eta=h+b

        index_max = eta[:,my/4].argmax()
        xm=x[index_max]

        pl.plot(x-xm,eta[:,my/4],lw=3,color=colors[wave-1])
    #
    pl.ylim([0.74,0.8225])
    pl.xlim([-3,3])
    pl.xlabel('$x-x_m$',fontsize=30)
    pl.ylabel('$\eta$',fontsize=30)
    pl.xticks(size=30); pl.yticks(size=30)
    pl.yticks([0.74,0.76,0.78,0.8,0.82])
    pl.tight_layout()
    pl.savefig('scaling_left_fig.png',bbox_inches="tight")
    
    # *************************************** #
    # ********** PLOT SCALED WAVES ********** #
    # *************************************** #
    pl.clf()
    for index in np.arange(1,num_waves+1):
        sol=Solution(frame,file_format='petsc',read_aux=False,path=path,file_prefix='wave'+str(index))
        h=sol.state.q[0,:,:]
        hu=sol.state.q[1,:,:]
        x=sol.state.grid.x.centers
        y=sol.state.grid.y.centers
        my=len(y)
        mx=len(x)
        b=bathymetry(x,y)[0,:,:]
        eta=h+b

        index_max = eta[:,my/4].argmax()
        xm=x[index_max]

        # compute normalization factor
        wave = (eta-mwl)[:,my/4]
        A = wave.max()
        norm_h = wave/A
        norm_x = np.sqrt(A)*(x-xm)

        # append data for curve fitting
        [all_waves_norm_x.append(i) for i in norm_x]
        [all_waves_norm_h.append(i) for i in norm_h]

        lines.append(pl.plot(norm_x,norm_h,lw=3,color=colors[index-1])[0])
    #
    # curve fitting
    sech2_data = curve_fit(fun,all_waves_norm_x,all_waves_norm_h)[0]
    fitted_sech2 = fun(norm_x,sech2_data[0],sech2_data[1])
    lines.append(pl.plot(norm_x,fitted_sech2,'--k',lw=6)[0])

    # format plot
    pl.ylim([-0.1,1.05])
    pl.xlim([-0.5,0.5])
    pl.xlabel('$\hat{x}$',fontsize=30)
    pl.ylabel('$\hat{\eta}$',fontsize=30)
    pl.xticks(size=30); pl.yticks(size=30)
    pl.tight_layout()
    pl.savefig('scaling_right_fig.png',bbox_inches="tight")
    
    # format figure
    #pl.tight_layout()
    #pl.subplots_adjust(wspace=0.25)
    #pl.figlegend(handles=(lines[0], lines[1], lines[2], lines[3]),
    #              labels=('Diffracton 1',
    #                      'Diffracton 2',
    #                      'Diffracton 3',
    #                      'Diffracton 4'),
    #              loc='upper center', ncol=4, labelspacing=20.,
    #              fontsize=30)
    #pl.savefig('scaling.png',bbox_inches="tight")

if __name__== "__main__":
    frame=340
    plot_waves(frame,'./_output_isolated_waves/',4)
