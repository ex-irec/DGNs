# coding: utf-8

import time
import argparse
import pickle

#from data_construction.raw_molecules import MoleculeDatasetDGL, MoleculeDataset
from realworld_benchmark.data.molecules import MoleculeDatasetDGL, MoleculeDataset

parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', type=str, default='ZINC', help='name of dataset')

args = parser.parse_args()
DATASET_NAME = args.name
dataset = MoleculeDatasetDGL(DATASET_NAME)

print(len(dataset.train))
print(len(dataset.val))
print(len(dataset.test))

print(dataset.train[0])
print(dataset.val[0])
print(dataset.test[0])

num_atom_type = 28
num_bond_type = 4

start = time.time()
with open('raw_data/'+DATASET_NAME+'.pkl','wb') as f:
    pickle.dump([dataset.train,dataset.val,dataset.test,num_atom_type,num_bond_type],f)
print('Time (sec):',time.time() - start)
