from clawpack.petclaw.solution import Solution
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as pl
import numpy as np
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

def get_diff(frame,sol_ref,path,name_file,plot_path=None):
    sol=Solution(frame,file_format='petsc',read_aux=False,path=path)
    h=sol.state.q[0,:,:]
    h_ref=sol_ref.state.q[0,:,:]
    x=sol.state.grid.x.centers
    y=sol.state.grid.y.centers

    b=bathymetry(x,y)[0,:,:]
    eta=h+b
    eta_ref=h_ref+b
    
    my=len(y)

    index_max_ref = eta_ref[:,my/4].argmax()
    index_max = eta[:,my/4].argmax()

    eta=np.roll(eta,index_max_ref-index_max,axis=0)
    index_max = eta[:,my/4].argmax()

    if plot_path is not None:
        pl.clf()
        pl.plot(x,eta_ref[:,my/4],'-k')
        pl.plot(x,eta[:,my/4],'-r')
        pl.ylim([0.74,1.025*eta_ref[index_max_ref,my/4]])
        pl.xlim([x[index_max]-4,x[index_max]+4])
        pl.savefig(plot_path+'figNx'+str(Nx)+'_'+str(frame)+'.png')
    #
    L2_error = np.linalg.norm(eta-eta_ref)/np.linalg.norm(eta_ref)
    L1_error = np.sum(np.abs(eta-eta_ref))/np.sum(np.abs(eta_ref))
    Linf_error = np.max(np.abs(eta-eta_ref))/np.max(np.abs(eta_ref))

    file=open(name_file,'a')
    file.write(str(L1_error)+','+str(L2_error)+','+str(Linf_error)+','+str(eta[index_max,my/4])+'\n')
    file.close()


if __name__== "__main__":
    if not os.path.exists('./_plots'): os.mkdir('_plots')
    
    for Nx in [64,128]:
        print ("**************************************************************")
        print ("********** Measuring shape in simulation with Nx="+str(Nx)+" **********")
        print ("**************************************************************")
        if not os.path.exists('./_plots/Nx'+str(Nx)+'/'): os.mkdir('./_plots/Nx'+str(Nx)+'/')
            
        # Read reference
        sol_ref=Solution(340,file_format='petsc',read_aux=False,path='./_output/Nx'+str(Nx)+'/')

        # Create file
        file_name='change_in_shape_diff1_Nx'+str(Nx)+'.txt'
        file=open(file_name,'w')
        file.close()

        # Time loop
        from_frame = 340
        to_frame = 440
        for i in xrange(from_frame,to_frame+1):
            print i
            get_diff(i,sol_ref,'./_output/Nx'+str(Nx)+'/',file_name,plot_path='./_plots/Nx'+str(Nx)+'/')
    #
