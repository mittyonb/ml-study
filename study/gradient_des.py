#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

def hyp(the0, the1, ins):
    return the0 + the1*ins
    
def renew_the0(the0, the1, x , y, length):
    z = 0
    for i in range(length):
        z =z + (hyp(the0,the1,x[i]) - y[i])
    return z/length

def renew_the1(the0, the1, x , y, length):
    z = 0
    for i in range(length):
        z =z + (hyp(the0,the1,x[i]) - y[i])*x[i]
    return z/length


def cost_J(the0, the1, x , y, length):
    z = 0
    for i in range(length):
        z =z + (hyp(the0,the1,x[i]) - y[i])*(hyp(the0,the1,x[i]) - y[i])
    return z/(2*length)
        
x = [] 
y = []
result1 = []
result2=[]
alpha = 0.000001
cnt = 0
test = []
ans = []
cost = []
the0 = random.uniform(-0.5,0.5)
the1 = random.uniform(-0.5,0.5)
plt.ylim(-100, 1000)
plt.xlim(0, 1000)

for i in range(50):
    x.append(random.randint(0,1000))
    y.append(random.randint(0,1000))
    test.append(random.randint(0,1000))
x.sort()
y.sort()
test.sort()
plt.plot(x,y,'o')
    
for i in range(max(x)+10):
    result1.append(hyp(the0, the1, i))            
plt.plot(result1, 'r')

for i in range(50):
    cost.append(cost_J(the0,the1, x, y, len(x)))
    temp = the0 - alpha*renew_the0(the0,the1, x, y, len(x))
    the1 = the1 - alpha*renew_the1(the0,the1, x, y, len(x))
    the0 = temp    
    cnt = cnt + 1
    print "count=" + str(cnt) + "   the0=" + str(the0) + "   the1=" + str(the1)
    
for i in range(max(x)+10):
    result2.append(hyp(the0, the1, i))

for i in test:
    ans.append(hyp(the0,the1, i))
            
cnt = 0
plt.plot(result2, 'm')
plt.show()

plt.plot(x,y,'o')
plt.plot(test,ans,'ro')
plt.show()

plt.plot(cost,'o')
plt.show()