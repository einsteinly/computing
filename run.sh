#!/bin/bash
# Written on Mac OS by Einsteinly
# Bash script for running tests and demonstration python3 files.
# Before running this for the first time, change the permissions by 
#	chmod 700 ./run.sh

echo "*********************************"
echo "*********************************"
echo "Running python3 tests."
python3 -m pytest .
echo "*********************************"
echo "*********************************"
echo "Running script $1."
python3 ./$1