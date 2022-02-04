import time

start_time = time.time()

import MDAnalysis as mda
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA

import numpy as np

print("--- %s seconds ---" % (time.time() - start_time))

temp = 260

file1 = 'eq_'+np.str(temp)+'.gro'
file2 = 'eq_'+np.str(temp)+'.trr'

print('loading of the universe')

u = mda.Universe(file1, file2)

hbonds = HBA(universe=u,
             donors_sel='resname SOl and name OW',
             hydrogens_sel='resname SOL and name HW1 HW2',
             acceptors_sel='resname SOL and name OW',
             d_h_cutoff=1.2)
hbonds.run()

print("--- %s seconds ---" % (time.time() - start_time))

# get average angle per temperature:
angle = 0.0
for i in range(0,len(hbonds.hbonds)):
    angle = angle + hbonds.hbonds[i, 5]

ave_angle_temp = angle / len(hbonds.hbonds)
print("Average angle over the all simulation %f in degree at %d K" % (ave_angle_temp, temp))

#get average number of bonds per temperature:

hb_nb = sum(hbonds.count_by_time()) / len(hbonds.count_by_time())
print("Average number of Hydrogen bonds at %d K: %f" %(temp, hb_nb))