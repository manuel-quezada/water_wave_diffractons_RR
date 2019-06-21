# water_wave_diffractons_RR
This repository is meant for reproducibility of the paper **Solitary water waves created by variations in bathymetry**.

## About the paper.
* A pre-print can be found here XX.

## Organization of the repository
The repository has the following main folders:

* KdV. This folder contains all instructions to create the results related to the KdV equation (and comparisons to it). 
* misc. This folder has miscellaneous code to cut the SW diffractons, do the scaling and generate different plots of geometries, notation, etc.
* Proteus. This folder has instructions to install Proteus and checkout the specific commit that we use in this work. It also contains the scripts to run the 2D and the 3D Navier-Stokes simulations.
* PyClaw. This folder has all the code that uses PyClaw for different sections.

## Scientific computing libraries
In this work we use different libraries and software to generate the results and plots.
* PyClaw. This is a hyperbolic solver based on Riemann solvers. See http://www.clawpack.org/pyclaw.
* Proteus. This is a finite element toolkit for solving PDEs. See https://proteustoolkit.org/ and https://github.com/erdc/proteus. 
* We also use Matlab and Paraview.
