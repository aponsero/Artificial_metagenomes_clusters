#!/bin/bash

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l select=1:ncpus=28:mem=168gb 
#PBS -l walltime=24:00:00
#PBS -M aponsero@email.arizona.edu
#PBS -m bea


HOST=`hostname`
LOG="$STDOUT_DIR/${HOST}.log"
ERRORLOG="$STDERR_DIR/${HOST}.log"

if [ ! -f "$LOG" ] ; then
    touch "$LOG"
fi
echo "Started `date`">>"$LOG"
echo "Host `hostname`">>"$LOG"

#load python environment
source activate python2

# run script
RUN="$WORKER_DIR/generate_vectors.py"

python $RUN $PROFILE $NB_GROUPS $NB_METAGENOMES
echo "Finished `date`">>"$LOG"
