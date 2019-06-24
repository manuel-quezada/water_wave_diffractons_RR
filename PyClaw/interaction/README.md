# Interaction of SW diffractons

* From PyClaw/formation, run the simulation up to at least t=365 with variance 2.
* From misc/cutting, cut the first two diffractons for the frames t=340 and 365.
* Make a folder called ./_output/isolated_waves and place all cut waves inside such folder.
* Run `set_ICs.py`
* Edit `run_sw_eqns.py` to select the simulation to run (1:counter-propagating, 2:co-propagating or 3:reference).
* Copy the files from either _output/co-propagating, _output/counter-propagating or _output/reference to _output (depending on the simulation to be run).
* Run `run_sw_eqns.py`
* Once the three simulations are finished, run `run_plots.py` to generate the plots in the paper.
