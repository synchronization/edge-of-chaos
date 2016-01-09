#!/usr/local/bin/python2.7

__author__ = "Roozbeh Daneshvar"
__email__ = "roozbeh.daneshvar@gmail.com"

import random
import math as math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

# -----------------------------

def sine_map_function(x, a):
    return a * math.sin(math.pi * x)

# -----------------------------

def tent_map_function(x, a):
    return a * min(x, 1 - x)

# -----------------------------

def logistic_map_function(x, a):
    return a * x * (1.0 - x)

# -----------------------------

def dynamics_function(x, a):
#    return logistic_map_function(x, a)
    return tent_map_function(x, a)
#    return sine_map_function(x, a)

# -----------------------------

def iterations(steps = 1000, initial_x = 0.38, initial_a = 3.8, r = 0.005):
    x_ = initial_x
    x = []

    a_ = initial_a
    a = [a_]

    for n in range(steps):
        f = x_
    
        for k in range(1, 33):
#            x_ = a[n] * x_ * (1.0 - x_)
            x_ = dynamics_function(x_, a[n])
        
        x_ = x_ + (random.random() - 0.5) * r
    
        if x_ > 1:
            x_ = 0.999
        if x_ < 0:
            x_ = 0.001
    
        f = f - x_
    
        x.append(x_)
        a.append(a[n] + 0.1 * f)
    
        if a[n+1] < 0:
            a[n+1] = 0.0
        
        if a[n+1] > 2:
            a[n+1] = 2.0
    
        for k in range(1, 32):
#            x_ = a[n] * x_ * (1.0 - x_)
            x_ = dynamics_function(x_, a[n])

    return a

# -----------------------------

def plot_parameters(inputs):
    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)
    for a in inputs:
        plt.plot(a)
    plt.grid()
    plt.show()

# -----------------------------

#a1 = iterations(steps = 1000, r = 0.0)
#a2 = iterations(steps = 1000, r = 0.005)

n = 16000
randomness = 0.00005

a = []
#initial_as = [0.3, 0.7, 1.0, 1.4]
initial_as = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
#for ia in initial_as:
#    a.append(iterations(steps = n, initial_x = 0.38, initial_a = ia, r = randomness))

#plot_parameters(a)

#print np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))



#t = np.arange(256)
#sp = np.fft.fft(np.sin(t))
#freq = np.fft.fftfreq(t.shape[-1])
#plt.plot(freq, sp.real, freq, sp.imag)
#plt.show()




Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0, 1, Ts) # time vector

print 't: ', t

ff = 5;   # frequency of the signal
y = np.sin(2 * np.pi * ff * t) + np.sin(2 * np.pi * 9 * t)

#y = [0, 1, 2, 1, 0, -1, -2, -1]
y = iterations(steps = len(t), initial_x = 0.38, initial_a = 1.7, r = 0)
print 'y: ', y

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(n/2)]

print 'frq: ', frq
print 'Y: ', Y
print 'abs(Y): ', abs(Y)

plot_parameters([abs(Y)])

# -----------------------------
