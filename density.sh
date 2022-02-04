#!/bin/bash
 

tmp=265

echo "Yoo"
#gromacs commands  
    gmx energy -f mdout_298.edr -o density.xvg
    echo | -e "21\n" 
