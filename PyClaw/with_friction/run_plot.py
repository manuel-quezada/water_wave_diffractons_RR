#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from plot import *

    print('**********************')
    print('**********************')
    print('Plotting solution ...')

    for friction in [0.0, 0.025, 0.033, 0.05]:
        path = './_output/cf_'+str(friction)
        name='friction_cf'+str(friction)+'_time200'
        plot_q(frame=200,
               plot_slices=True,
               plot_pcolor=False,
               path=path,
               name=name,
               slices_ylimits=[0.74,0.81],
               slices_xlimits=[30,70],
               ylabel=None,
               plot_title=False,
               xShift=400)
