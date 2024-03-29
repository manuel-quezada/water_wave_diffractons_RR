# Results related to the KdV equation

* Inside the folder ./spectral:
  * Edit `solver.m` to select: name_solution and mwl (mean water level).
  * Run `solver.m` to generate uKdV_XX.csv and xKdV_XX.csv (XX=name_solution).
  * Copy the generated .csv data into KdV/plotting/data_spectral.
* Inside PyClaw/versus_KdV run `run_sw_eqns.py`.
* Inside PyClaw/versus_KdV run `run_plot.py` to generate .csv data.
* Copy the .csv data generated in PyClaw/versus_KdV into KdV/plotting/data_FV.
* Inside Proteus/2D/comparison_versus_KdV edit `run.sh` to select one of the two 2D-NS simulations to run.
* For each 2D-NS simulation open the data in Paraview and export .csv data files of the zero contour of phi at t=30.
  * Note: the names of the .csv files generated by Paraview must be: nsDeep_contour_t300.csv and nsShallow_contour_t300.csv.
* Place the .csv files generated by Paraview inside KdV/plotting/data_FEM.
* Run `KdV/plotting/plot.py` to generate the figures in the paper.
