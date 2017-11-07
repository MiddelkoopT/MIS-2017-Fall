#!/bin/bash

#SBATCH -J baseball

echo === sbatch baseball $SLURM_JOB_ID $(date)
module list

srun bash download-data.sh
srun python3 build-database.py
srun python3 prepare-data.py

module load julia/julia-0.5.0
srun julia compute.jl

