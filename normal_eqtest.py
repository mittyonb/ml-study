#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:42:04 2017

@author: mitsunobu
"""

import numpy as np

X = np.array([[ 1, 1, 1, 1, 1],
              [ 1, 2, 3, 4, 5],
              [10,13,15,17,19],
              [ 3, 7,13,16,19],
              [56,42,35,26,11]]).transpose()
y = np.array([2.1,3.4,5.5,6.0,7.8])
Theta =  np.dot(np.dot(np.linalg.inv(np.dot(X.transpose(),X)) , X.transpose()) , y)
print Theta
print np.dot(X,Theta)