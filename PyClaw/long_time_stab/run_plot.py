#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from plot import *
    if not os.path.exists('./_plots'): os.mkdir('_plots')
    
    from_frame = 340
    to_frame   = 440
    frames=xrange(from_frame,to_frame+1)

    print('**********************')
    print('**********************')
    print('Plotting solution ...')
    for i in frames:
        plot_q(frame=i,
               plot_slices=True,
               plot_pcolor=False,
               path='./_output/')
        print ('frame '+str(i)+' plotted')
    #
    
