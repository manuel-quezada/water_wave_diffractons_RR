# Speed-amplitude relations

* This code works after cutting the diffractons.
* Create a folder called ./_output.
* The following is to create the data for each diffracton. It must be repeated for all the waves. I consider (for instance) wave1.
  * Place the wave1 files (wave1.pkl0638, wave1.ptc0638, wave1.ptc0638.info) inside ./_output.
  * Edit and run `run_sw_eqns.py` to select which wave will be run (wave1 in this example).
  * Once the simulation is finished, the data will be in ./_output.
  * Create a folder called ./_output/wave1 and move the generated data inside such folder.
* Create the data for all five diffractons and place it inside the corresponding folders.
* Run `measure_speed.py` to create txt files with the measurements.
* Run `plot_speed.py` to generate the speed-amplitude plot.
