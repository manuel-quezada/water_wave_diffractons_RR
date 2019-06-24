#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from plot import *
        
    if not os.path.exists('./_plots'): os.mkdir('_plots')
    from_frame = 0
    to_frame   = 200
    frames=xrange(from_frame,to_frame+1)

    if True:
        xLim = None
        xShift=0.0
        yLim = [0.54,0.60]
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
                   bathymetry_type=2)
            print ('frame '+str(i)+' plotted')
    #
    
    if True:
        xShift=300
        xLim=[40,100]
        yLim=[0.54,0.60]
        name='diffractons_on_channel'
        plot_q(frame=200,
               plot_slices=True,
               plot_pcolor=True,
               path='./_output/',
               xShift=xShift,
               slices_xlimits=xLim,
               slices_ylimits=yLim,
               bathymetry_type=2,
               name=name)
    #
