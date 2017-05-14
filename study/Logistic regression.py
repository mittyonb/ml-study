#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:27:01 2017

@author: mitsunobu
"""
import numpy as np
import matplotlib.pyplot as plt
import math
#仮説関数
def hyptest(theta,x):
    return 1.0/(1+math.exp(-x))
    
def hyp(theta,x):
    return 1.0/(1+math.exp(-1*np.dot(theta,x.T)))

#コスト関数    
def cost(theta, x, y):
     return -y*math.log(hyp(theta,x)) - (1-y)*math.log(1 - hyp(theta,x))
    
def failcost(theta,x,y):
    return (hyp(theta,x) - y)/2
    
#コスト関数の偏微分
def newtheta(theta, x, y,length,num):
 
    alpha = 0.01
    result = 0
    for i in range(length):
        result = result + ((hyp(theta,x.T[i]) - y.T[i]) * x.T[i][num])
    return theta[num] - (alpha * result)

#コスト関数の総和
def J(theta,x,y,length):
    result = 0
    for i in range(length):
        result = result + cost(theta,x.T[i],y.T[i])
    return result/length

#決定境界の直線        
def boundfun(theta,i):
    return (theta[1]*i + theta[0])/-theta[2]

def drawplot(x,y,theta,inith):
    bound = []
    plt.grid()
    plt.ylim(0, 5)
    plt.xlim(0, 5)
    for i in range(length):
        if y.T[i] == 0:
            plt.plot(x[1][i],x[2][i],'ro')
        elif y.T[i] == 1:
            plt.plot(x[1][i],x[2][i],'bx') 

    for i in range(-10,11):
        bound.append(boundfun(theta,i))

    plt.plot(range(-10,11),inith,'m--')        
    plt.plot(range(-10,11),bound,'m')
 
#サンプルの生成
fig, ax = plt.subplots(1, 1)
theta = np.array([-1.0,1.0,1.0])
x = np.array([[1,1,1,1,1,1,1,1,1],
              [1,1,1,2,2.2,2,3,3,3],
              [1,2,3,1,1.8,3,1,2,3]])
length = len([0,0,1,0,1,1,1,1,1])
y = np.array([[1,1,1,0,0,1,0,0,1]])
test = []
bound = []
fig = plt.figure()
ims = []

for i in range(-10,11):
    bound.append(boundfun(theta,i))    

drawplot(x,y,theta,bound)

#thetaの更新
for _ in range(100):
    temp = []
    for i in range(3):
        temp += newtheta(theta,x,y,length,i).tolist()
    theta = np.array(temp).T
    plt.cla()
    drawplot(x,y,theta,bound)
    plt.pause(.5)

plt.show()
