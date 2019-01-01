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
import noise_adder as nadd
import random

count = 0
n_duplicates = 2 #number of noisy duplicates of each image

sigma_fact_range = [0, 0.2]
mu_fact_range = [0 , 0.2]

obj_noise = nadd.NoiseAdder()

# Defining the conotrlling parameters for noise addition

list_of_files = glob.glob('../data/raw/2D_Seismic_Alaska/slices/*')
input_path = '../data/processed/2D_Seismic_Alaska/input/'
output_path = '../data/processed/2D_Seismic_Alaska/output/'

noisefree_indices = [] # to store the indices of files that contain noisefree data

for file in list_of_files:
    
    # load the data from the npy file
    raw_data = np.load(file)
    #raw_data = raw_data[::4, ::4]
    
    # add the noisefree file into the dataset
    fname_i = input_path + 'data_' + str(count) + '.npy'
    fname_o = output_path + 'data_' + str(count) + '.npy'
    np.save(fname_i, raw_data)
    np.save(fname_o, raw_data)
    count += 1
        
    # Creating n_duplicates with noise
    for i in range(n_duplicates):
                    
        # generate a random number to choose which noise to add
        randno = random.randint(1, 1)
        if randno <= 2:
            # Adding normal noise
            sigma_fact = sigma_fact_range[0] + (sigma_fact_range[1] - sigma_fact_range[0]) * random.uniform(0, 1)
            mu_fact = mu_fact_range[0] + (mu_fact_range[1] - mu_fact_range[0]) * random.uniform(0, 1)
            img_new = obj_noise.add_normal_noise(raw_data, sigma_fact, mu_fact)
            fname_i = input_path + 'data_' + str(count) + '.npy'
            fname_o = output_path + 'data_' + str(count) + '.npy'
            np.save(fname_i, img_new)
            np.save(fname_o, raw_data)
            
            count = count + 1
            print(count)
        
#    # Creating n_duplicates with noise
#    for i in range(n_duplicates):
#                    
#        # generate a random number to choose which noise to add
#        randno = random.randint(1, 1)
#        if randno <= 2:
#            # Adding normal noise
#            sigma_fact = sigma_fact_range[0] + (sigma_fact_range[1] - sigma_fact_range[0]) * random.uniform(0, 1)
#            mu_fact = mu_fact_range[0] + (mu_fact_range[1] - mu_fact_range[0]) * random.uniform(0, 1)
#            img_new = obj_noise.add_uniform_noise(raw_data, sigma_fact, mu_fact)
#            #plt.imshow(img_new)
#            fname_i = input_path + 'data_' + str(count) + '.npy'
#            fname_o = output_path + 'data_' + str(count) + '.npy'
#            np.save(fname_i, img_new)
#            np.save(fname_o, raw_data)
#            
#            count = count + 1
#            print(count)

