# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:16:35 2018

"""

'''
This script is used to create the training, validation and test dataset for the
synthetic data stored in data/raw/cseg_paper_fault_dyke_fold_model

'''

# importing the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import glob

count = 0

list_of_files = glob.glob('../data/raw/cseg_paper_fault_dyke_fold_model/*')
for file in list_of_files:
    
    # load the data from the npy file
    raw_data = np.load(file)
    print(count)
    count += 1
