# 2D-NS simulations as reference versus 3D simulations

* Create a folder called ./FEM_DATA/
* Edit the script `run.sh` to select one of the six simulations.
* Run the script `run.sh`.
* For each simulation, open the data in Paraview and export the zero contour of phi at t=7.
  * The files exported from Paraview must be called: varXX_bA0p00.csv, varXX_bA0p250.csv, varXX_bA0p50.csv, where XX={2,4}
  * The .csv files must be placed inside the folder ./FEM_DATA/
* Run `plot_extracted_2D_FEM.py` to create the figures in the paper
