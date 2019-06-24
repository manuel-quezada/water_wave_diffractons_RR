#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from sw_eqns import *
    sig2=2
    
    sw_eqns(# General parameters for simulatiuon #
        final_time=30.0,
        nDOut=30,
        restart_from_frame=None,
        # about initial condition
        A=0.05,
        sig2=sig2,
        mwl=0.75)
