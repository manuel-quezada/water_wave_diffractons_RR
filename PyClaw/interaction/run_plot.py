#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from plot import *
    import sw_eqns
    if not os.path.exists('./_plots'): os.mkdir('_plots')
    print('**********************')
    print('**********************')
    print('Plotting solution ...')

    # ********************************************** #
    # ********** PLOTS FOR TIME EVOLUTION ********** #
    # ********************************************** #
    if False:
        simulation = 1 #1: counter-propagating, 2: co-propagating, 3: reference
        assert simulation in [1,2,3]

        from_frame = 0
        if simulation == 1:
            to_frame   = 15
            path='./_output/counter-propagating/'
        elif simulation == 2:
            to_frame   = 700
            path='./_output/co-propagating/'
        else:
            to_frame   = 700
            path='./_output/reference/'
        #
        frames=xrange(from_frame,to_frame+1)
        for i in frames:
            plot_q(frame=i,
                   path=path,
                   plot_slices=True,
                   plot_pcolor=False)
            print ('frame '+str(i)+' plotted')
        #
    #

    # ********************************************************** #
    # ********** PLOTS FOR CO-PROPAGATING INTERACTION ********** #
    # ********************************************************** #
    xMinusLim=[40,20,15]
    xPlusLim=[75,55,50]
    ylim=[0.74,0.82]
    xShifts = [0,800,1400]
    index=0
    for frame in [0,340,600]:
        # reference solution #
        path='./_output/reference/'
        sol=Solution(frame,file_format='petsc',read_aux=False,path=path)
        x=sol.state.grid.x.centers; y=sol.state.grid.y.centers
        mx=len(x); my=len(y)

        h=sol.state.q[0,:,:]
        eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]

        pl.figure(figsize=(15,5))
        pl.plot(x+xShifts[index],eta[:,3*my/4],'--r',lw=3)
        pl.plot(x+xShifts[index],eta[:,my/4],'--b',lw=3)
        pl.title("t= "+str(sol.state.t),fontsize=25)
        pl.ylabel('$\eta$',fontsize=30)
        pl.xticks(size=25); pl.yticks(size=25)
        pl.tight_layout()
        pl.axis([xMinusLim[index]+xShifts[index],xPlusLim[index]+xShifts[index],ylim[0],ylim[1]])

        # co-propagating #
        path='./_output/co-propagating/'
        sol=Solution(frame,file_format='petsc',read_aux=False,path=path)
        h=sol.state.q[0,:,:]
        eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]
        pl.plot(x+xShifts[index],eta[:,3*my/4],'-r',lw=3)
        pl.plot(x+xShifts[index],eta[:,my/4],'-b',lw=3)

        pl.savefig('co-prop_'+str(frame)+'_slices.png' ,bbox_inches="tight")
        pl.close()
        index+=1
    #
    pl.figure(figsize=(15,5))
    sol=Solution(600,file_format='petsc',read_aux=False,path='./_output/reference')
    h=sol.state.q[0,:,:]
    eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]
    pl.plot(x+xShifts[-1],eta[:,3*my/4],'--r',lw=3)
    pl.plot(x+xShifts[-1],eta[:,my/4],'--b',lw=3)
    sol=Solution(600,file_format='petsc',read_aux=False,path='./_output/co-propagating')
    h=sol.state.q[0,:,:]
    eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]
    pl.plot(x+xShifts[-1],eta[:,3*my/4],'-r',lw=3)
    pl.plot(x+xShifts[-1],eta[:,my/4],'-b',lw=3)
    pl.title("t= "+str(sol.state.t),fontsize=25)
    pl.ylabel('$\eta$',fontsize=30)
    pl.xticks(size=25); pl.yticks(size=25)
    pl.tight_layout()
    pl.axis([1427,1441,0.745,0.78])
    pl.savefig('co-prop_zoomed_'+str(frame)+'_slices.png' ,bbox_inches="tight")
    pl.close()


    # *************************************************************** #
    # ********** PLOTS FOR COUNTER-PROPAGATING INTERACTION ********** #
    # *************************************************************** #
    xMinusLim=[40,40,40]
    xPlusLim=[75,75,75]
    ylim=[0.74,0.82]
    xShifts = [0,0,0]
    index=0
    for frame in [0,5,10]:
        # reference solution #
        path='./_output/reference/'
        sol=Solution(frame,file_format='petsc',read_aux=False,path=path)
        x=sol.state.grid.x.centers; y=sol.state.grid.y.centers
        mx=len(x); my=len(y)

        h=sol.state.q[0,:,:]
        eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]

        pl.figure(figsize=(15,5))
        pl.plot(x+xShifts[index],eta[:,3*my/4],'--r',lw=3)
        pl.plot(x+xShifts[index],eta[:,my/4],'--b',lw=3)
        pl.title("t= "+str(sol.state.t),fontsize=25)
        pl.ylabel('$\eta$',fontsize=30)
        pl.xticks(size=25); pl.yticks(size=25)
        pl.tight_layout()
        pl.axis([xMinusLim[index]+xShifts[index],xPlusLim[index]+xShifts[index],ylim[0],ylim[1]])

        # co-propagating #
        path='./_output/counter-propagating/'
        sol=Solution(frame,file_format='petsc',read_aux=False,path=path)
        h=sol.state.q[0,:,:]
        eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]
        pl.plot(x+xShifts[index],eta[:,3*my/4],'-r',lw=3)
        pl.plot(x+xShifts[index],eta[:,my/4],'-b',lw=3)

        pl.savefig('counter-prop_'+str(frame)+'_slices.png' ,bbox_inches="tight")
        pl.close()
        index+=1
    #
    pl.figure(figsize=(15,5))
    sol=Solution(10,file_format='petsc',read_aux=False,path='./_output/reference')
    h=sol.state.q[0,:,:]
    eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]
    pl.plot(x+xShifts[-1],eta[:,3*my/4],'--r',lw=3)
    pl.plot(x+xShifts[-1],eta[:,my/4],'--b',lw=3)
    sol=Solution(10,file_format='petsc',read_aux=False,path='./_output/counter-propagating')
    h=sol.state.q[0,:,:]
    eta=h+sw_eqns.bathymetry(x,y,bathymetry_type=0)[0,:,:]
    pl.plot(x+xShifts[-1],eta[:,3*my/4],'-r',lw=3)
    pl.plot(x+xShifts[-1],eta[:,my/4],'-b',lw=3)
    pl.title("t= "+str(sol.state.t),fontsize=25)
    pl.ylabel('$\eta$',fontsize=30)
    pl.xticks(size=25); pl.yticks(size=25)
    pl.tight_layout()
    pl.axis([47,68,0.745,0.78])
    pl.savefig('counter-prop_zoomed_'+str(frame)+'_slices.png' ,bbox_inches="tight")
    pl.close()

