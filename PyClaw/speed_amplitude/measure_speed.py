from clawpack.petclaw.solution import Solution
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as pl
import numpy as np

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

def get_max(frame,name,path='./_output/',file_prefix='claw'):
    sol=Solution(frame,file_format='petsc',read_aux=False,path=path,file_prefix=file_prefix)
    x=sol.state.grid.x.centers; y=sol.state.grid.y.centers
    mx=len(x); my=len(y)

    h=sol.state.q[0,:,:]
    u=sol.state.q[1,:,:]    
    b=bathymetry(x,y)[0,:,:]
    eta=h+b

    y_index_max = eta.max(0).argmax()
    x_index_max = eta[:,y_index_max].argmax()    
    
    file=open(name+'.txt','a')
    file.write(str(sol.state.t)+' '+str(x[x_index_max])+' '+str(eta[x_index_max,y_index_max])+' '+str(u[x_index_max,y_index_max])+'\n')
    file.close()

def record_max(from_frame,to_frame,name,path='./_output/',file_prefix='claw'):
    t=np.zeros(to_frame-from_frame+1)
    x=np.zeros(to_frame-from_frame+1)
    file=open(name+'.txt','w')
    file.close()
    for i in xrange(from_frame,to_frame+1):
        print '     ', str(i)
        get_max(i,name,path=path,file_prefix=file_prefix)
    print ''

if __name__== "__main__":    
    from_frame = 638
    to_frame = 738

    print 'recording max points for wave 1'
    record_max(from_frame,to_frame,'wave1',path='./_output/wave1/')

    print 'recording max points for wave 2'
    record_max(from_frame,to_frame,'wave2',path='./_output/wave2/')

    print 'recording max points for wave 3'
    record_max(from_frame,to_frame,'wave3',path='./_output/wave3/')

    print 'recording max points for wave 4'
    record_max(from_frame,to_frame,'wave4',path='./_output/wave4/')

    print 'recording max points for wave 5'
    record_max(from_frame,to_frame,'wave5',path='./_output/wave5/')    
