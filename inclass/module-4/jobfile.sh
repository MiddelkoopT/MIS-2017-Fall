#!/bin/bash

#SBATCH -J baseball

echo === sbatch baseball $SLURM_JOB_ID $(date)
module list

srun bash download-data.sh
srun python3 build-database.py
srun python3 prepare-data.py

## Run Julia
module load julia/julia-0.5.0
srun julia compute.jl

## Run R analysis (no real analysis here)
module load R/R-3.2.3 
srun R --no-save -f simple.R 
