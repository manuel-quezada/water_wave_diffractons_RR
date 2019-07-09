mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_3D.py -l5 -v -F -O petsc.options.asm -C "final_time=18.0 dt_output=0.1 A=0.35 sig2=4.0 Lx=20.0 Ly=0.3 Lz=1.25 bA=0.0 bB=0.5 slipOnBottom=False he=0.01"
