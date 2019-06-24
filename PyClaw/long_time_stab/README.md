# Long time shape evolution and stability

* Make a directory called ./_output.
* The following must be repeated for two resolutions given by Nx=64 and Nx=128 grid cells. I consider, for instance, Nx=64.
  * Run the simulation with Nx=64 (see PyClaw/formation/). We use the initial condition with variance=2 for these results. 
  * Cut the first diffracton (see misc/cutting/) from frame 340 and place it inside ./_output.
  * Run `run_sw_eqns.py` to generate the simulation. The data will be placed inside ./_output.
  * Make a directory called ./_output/Nx64 and move the data generated from the simulation inside such folder.
* Repeat the process for both resolutions (Nx=64 and Nx=128).
* Run `shape.py` to generate some txt files and then run `error_in_shape.py` to compute the errors for both resolutions.
