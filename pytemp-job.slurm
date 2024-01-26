#!/bin/bash
#SBATCH --output=pytemp-job.out
#SBATCH --error=pytemp-job.err
#SBATCH --account standby
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:05:00
#SBATCH --mem=3G

date                                # Record job start time 
module load anaconda/2022.10-py39   # Use Anaconda
source activate pytemplate          # Load my environment
python pytemplate.py                # Run my code
date                                # Record job end time 
