# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:00:51 2018

@author: D.Gupta2
"""

import numpy as np
import matplotlib.pyplot as plt

class NoiseAdder:
    
    def __init__(self):
        # This is the initialization function for adding noise to input image
        print('Noise object intialized')
        
    def add_normal_noise(self, img, sigma_fact, mu_fact):
        '''
        This function adds Gaussian noise to the image
        
        '''
        amax_noise = np.max(img)
        sigma = amax_noise * sigma_fact
        mu = amax_noise * mu_fact
        # Gaussian noise with sigma and mu specified above
        noise = np.random.normal(mu, sigma, img.shape)
        

#        count, bins, ignored = plt.hist(noise, 30, density=True)
#        plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#             np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#             linewidth=2, color='r')
#        plt.show()
        #sys.exit(0)
        noise[noise<0] = 0
        img = img + noise
        #plt.imshow(img)
        return img
        
    def add_uniform_noise(self, img, sigma_fact, mu_fact):
        '''
        This function adds Gaussian noise to the image
        
        '''
        amax_noise = np.max(img)
        sigma = amax_noise * sigma_fact
        mu = amax_noise * mu_fact
        # Gaussian noise with sigma and mu specified above
        noise = np.random.uniform(0, sigma, img.shape)
        

#        count, bins, ignored = plt.hist(noise, 30, density=True)
#        plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#             np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#             linewidth=2, color='r')
#        plt.show()
        #sys.exit(0)
        noise[noise<0] = 0
        img = img + noise
        return img        