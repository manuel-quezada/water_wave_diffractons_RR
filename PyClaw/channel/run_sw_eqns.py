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
        # about bathymetry
        bathymetry_type=2,
        # about initial condition
        A=0.05,
        sig2=2.0,
        mwl=0.55)
