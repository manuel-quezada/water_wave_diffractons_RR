#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from sw_eqns import *
    simulation = 2 #1: counter-propagating, 2: co-propagating, 3: reference
    assert simulation in [1,2,3]
    
    if simulation == 1:
        sw_eqns(# General parameters for simulatiuon #
            outdir='./_output/counter-propagating',
            time_to_switch_BCs=10.0,
            final_time=15,
            nDOut=15,
            restart_from_frame=0)
    elif simulation == 2:
        sw_eqns(# General parameters for simulatiuon #
            outdir='./_output/co-propagating',
            time_to_switch_BCs=5.0,
            final_time=700,
            nDOut=700,
            restart_from_frame=0)
    else:
        sw_eqns(# General parameters for simulatiuon #
            outdir='./_output/reference',
            time_to_switch_BCs=5.0,
            final_time=700,
            nDOut=700,
            restart_from_frame=0)
