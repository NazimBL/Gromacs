#!/bin/bash


#SBATCH --job-name=_1b
#SBATCH --partition=talon
#SBATCH --exclusive
#SBATCH --time=28-00:00:00
#SBATCH --nodes=1
#SBATCH --error=./err.txt
#SBATCH --output=./out.txt
#SBATCH --mail-type=NONE
#SBATCH --mail-user=


module load intel/mpi/64
module load intel/mkl/64
export FI_PROVIDER-tcp

for i in {50,80,100,20,140,160,180,190,195,200,210,215,218,220,230,240,250,260}
do
	/home/export/apps/gromacs-5.1.4-gpu/bin/gmx convert-tpr -s eq_$i -extend 1000 -o eq_$i
	/home/export/apps/gromacs-5.1.4-gpu/bin/gmx mdrun -deffnm eq_$i
done
