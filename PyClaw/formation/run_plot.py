#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from plot import *
        
    if not os.path.exists('./_plots'): os.mkdir('_plots')
    from_frame = 0
    to_frame   = 400
    frames=xrange(from_frame,to_frame+1)

    if False:
        xLim = None
        xShift=0.0
        yLim = [0.74,0.82]
        if not os.path.exists('./_plots'): os.mkdir('./_plots')
        print('**********************')
        print('**********************')
        print('Plotting solution ...')
        for i in frames:
            plot_q(frame=i,
                   plot_slices=True,
                   plot_pcolor=False,
                   path='./_output/',
                   xShift=xShift,
                   slices_xlimits=xLim,
                   slices_ylimits=yLim,
                   X=None,
                   eta1=None, 
                   eta2=None)
            print ('frame '+str(i)+' plotted')
    #
    
    if True:
        xShift=700
        xLim=[40,100]
        yLim=[0.74,0.82]
        name='diffracton_var2'
        plot_q(frame=340,
               plot_slices=True,
               plot_pcolor=True,
               path='./_output/',
               xShift=xShift,
               slices_xlimits=xLim,
               slices_ylimits=yLim,
               pcolor_ylimits=[-0.25,0.25],
               name=name)
    #
