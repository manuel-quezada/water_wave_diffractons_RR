#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from sw_eqns import *
    friction_coeff=0.0 #0., 0.025, 0.033, 0.05
    
    sw_eqns(# General parameters for simulatiuon #
        final_time=200.0,
        nDOut=200,
        restart_from_frame=None,
        # about friction
        friction=True,
        friction_coeff=friction_coeff,
        # about initial condition
        A=0.05,
        sig2=2.0,
        mwl=0.75)
