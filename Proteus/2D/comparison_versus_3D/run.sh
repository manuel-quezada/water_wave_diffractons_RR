# Variance 2 #
mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_2D.py --path "./../" -l5 -v -F -O ./../petsc.options.asm -C "final_time=8.0 dt_output=0.1 Lx=20.0 bA=0.50 mwl=0.55 A=0.35 sig2=2.0 he=0.01 structured=False"
#mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_2D.py --path "./../" -l5 -v -F -O ./../petsc.options.asm -C "final_time=8.0 dt_output=0.1 Lx=20.0 bA=0.25 mwl=0.55 A=0.35 sig2=2.0 he=0.01 structured=False"
#mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_2D.py --path "./../" -l5 -v -F -O ./../petsc.options.asm -C "final_time=8.0 dt_output=0.1 Lx=20.0 bA=0.00 mwl=0.55 A=0.35 sig2=2.0 he=0.01 structured=False"

# Variance 4 #
#mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_2D.py --path "./../" -l5 -v -F -O ./../petsc.options.asm -C "final_time=8.0 dt_output=0.1 Lx=20.0 bA=0.50 mwl=0.55 A=0.35 sig2=4.0 he=0.01 structured=False"
#mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_2D.py --path "./../" -l5 -v -F -O ./../petsc.options.asm -C "final_time=8.0 dt_output=0.1 Lx=20.0 bA=0.25 mwl=0.55 A=0.35 sig2=4.0 he=0.01 structured=False"
#mpiexec -np 32 parun --TwoPhaseFlow -f gaussian_2D.py --path "./../" -l5 -v -F -O ./../petsc.options.asm -C "final_time=8.0 dt_output=0.1 Lx=20.0 bA=0.00 mwl=0.55 A=0.35 sig2=4.0 he=0.01 structured=False"

