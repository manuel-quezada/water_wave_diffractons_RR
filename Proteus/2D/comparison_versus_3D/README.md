# 2D-NS simulations as reference versus 3D simulations

* Create a folder called ./FEM_DATA/
* Edit the script `run.sh` to select one of the two simulations.
* Run the script `run.sh`.
* For each simulation, open the data in Paraview and save the data at t=6 as a csv file.
  * The files exported from Paraview must be called: var4_bA0p00.csv and var4_bA0p50.csv.
  * The .csv files must be placed inside the folder ./FEM_DATA/.
* Run `plot_extracted_2D_FEM.py` to create the figures in the paper
