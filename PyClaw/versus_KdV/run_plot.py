#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from plot import *
        
    if not os.path.exists('./_plots'): os.mkdir('_plots')
    from_frame = 0
    to_frame   = 30
    frames=xrange(from_frame,to_frame+1)

    X=[]
    eta1=[]
    eta2=[]
    
    if True:
        if not os.path.exists('./_plots'): os.mkdir('./_plots')
        print('**********************')
        print('**********************')
        print('Plotting solution ...')
        for i in frames:
            plot_q(frame=i,
                   plot_slices=True,
                   plot_pcolor=False,
                   path='./_output/',
                   slices_ylimits=[0.74,0.79],
                   X=X,
                   eta1=eta1,
                   eta2=eta2)
            print ('frame '+str(i)+' plotted')
    #
    # Save solution to csv files
    np.savetxt("X_FV.csv",np.array(X),delimiter=',')
    np.savetxt("eta1_FV.csv",np.array(eta1),delimiter=',')
    np.savetxt("eta2_FV.csv",np.array(eta2),delimiter=',')
