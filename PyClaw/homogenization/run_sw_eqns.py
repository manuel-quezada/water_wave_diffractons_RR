#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from sw_eqns import *
    
    sw_eqns(# General parameters for simulatiuon #
        final_time=200.0,
        nDOut=200,
        restart_from_frame=None,
        # about initial condition
        A=0.001,
        sig2=2,
        mwl=0.75)
