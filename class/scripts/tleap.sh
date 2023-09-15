#!/bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh

conda activate AmberTools22
tleap -f $1
conda deactivate

exit
