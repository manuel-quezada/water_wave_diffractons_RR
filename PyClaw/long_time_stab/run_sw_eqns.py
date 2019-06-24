#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('./../')

if __name__=="__main__":
    from sw_eqns import *
    
    sw_eqns(# General parameters for simulatiuon #
        final_time=440,
        nDOut=440,
        restart_from_frame=340,
        file_prefix='wave1')

