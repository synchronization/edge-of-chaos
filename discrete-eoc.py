#!/usr/local/bin/python2.7

__author__ = "Roozbeh Daneshvar"
__email__ = "roozbeh.daneshvar@gmail.com"

import random
import math as math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import sys

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
    return logistic_map_function(x, a)
#    return tent_map_function(x, a)
#    return sine_map_function(x, a)

# -----------------------------

def create_sequence(ic=0.5, a=1.5, n=10):
    """
    ic: initial condition (number to start with)
    a: parameter
    n: number of items in the list (iterations)

    returns: a list of numbers
    """
    result = [None] * n
    x = ic
    result[0] = x
    for i in range(1, n):
        x = dynamics_function(x, a)
        result[i] = x

    return result

# -----------------------------

def adapt(steps = 1000, initial_x = 0.38, initial_a = 3.8, r = 0.005, min_x = 0.0, max_x = 1.0, min_a = 0, max_a = 4.0):
    x_ = initial_x
    x = []
    a_ = initial_a
    a = [a_]

    for n in range(steps):
        f = x_
    
        for k in range(1, 33):
            x_ = dynamics_function(x_, a[n])
        
        x_ = x_ + (random.random() - 0.5) * r
    
        if x_ > max_x:
            x_ = max_x - 0.001#0.999
        if x_ < 0:
            x_ = min_x + 0.001#0.001
    
        f = f - x_
    
        x.append(x_)
        a.append(a[n] + 0.1 * f)
    
        if a[n+1] < min_a:
            a[n+1] = min_a
        if a[n+1] > max_a:
            a[n+1] = max_a
    
        for k in range(1, 32):
#        for k in range(0, 32):
            x_ = dynamics_function(x_, a[n])

    return a

# -----------------------------

def PRLadapt(steps=450, initial_x=0.25, initial_a=3.8, r=0.000, min_x=0.0, max_x=1.0, min_a=0.0, max_a=4.0, N=20):
    """
    A replication of PRL paper, according to the descriptions
    """

    x_ = initial_x
    x = []
    a_ = initial_a
    a = [a_]

    for n in range(steps):
        x_ = dynamics_function(x_, a[-1])
        
        if x_ > max_x:
            x_ = max_x - 0.001#0.999
        if x_ < min_x:
            x_ = min_x + 0.001#0.001
            
        x.append(x_)

        if n % N == 0 and n != 0:
            beta_n1 = 0.0
            for t in range(0, N):
                beta_n1 = beta_n1 + x[t + n - N + 0] * math.cos(2.0 * math.pi * t / N)

            beta_n1 = (2.0 / N) * beta_n1
            f = 0.1 * beta_n1
            new_a = a[-1] + f

            if new_a > max_a:
                new_a = max_a - 0.001
            if new_a < min_a:
                new_a = min_a + 0.001

            a.append(new_a)
    
    print 'x: ', x
    print 'a: ', a
    
    return a

# -----------------------------

def plot_time_series(inputs, title = ''):
    ax = plt.gca()
    ax.set_ylim([3.4, 4.1])
    ax.ticklabel_format(useOffset=False)
    for a in inputs:
        plt.plot(a)
    
    plt.title(title)
    plt.grid()
    plt.show()

# -----------------------------

def frequency_spectrum():
    n = 16000
    randomness = 0.00005

    a = []

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
    #y = adapt(steps = len(t), initial_x = 0.38, initial_a = 1.7, r = 0)
    result = create_sequence(ic=result[-1], a=3.2, n=len(t))
    y = result
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

    plot_time_series([abs(Y)])

# -----------------------------

if __name__ == "__main__":
    # transient
#    result = create_sequence(ic=0.5, a=3.2, n=100)
#    print 'transient result: ', result
    # actual
#    result = create_sequence(ic=result[-1], a=3.2, n=100)
#    print 'actual result: ', result

    #sys.exit(0)

    #a1 = adapt(steps = 1000, r = 0.0)
    #a2 = adapt(steps = 1000, r = 0.005)

#    seq = create_sequence(ic=0.37, a=3.5, n=100)
#    print seq

#    sys.exit(0)

    #initial_as = [0.3, 0.7, 1.0, 1.4]
    #initial_as = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
#    n = 450 * 20
    n = 6
    randomness= 0.000#0.005
    initial_as = [3.5, 3.8, 3.9]
#    initial_as = [3.5, 3.6, 3.7, 3.8, 3.9]
#    initial_as = [x*0.5 for x in range(2*x1, 2*x2+1)]
#    initial_as = np.arange(3.4, 4.0, 0.02)
    initial_xs = np.arange(0.2, 0.3, 0.05)

    for icx in initial_xs:#np.arange(0.2, 0.3, 0.05):
#    for icx in np.arange(0.94, 0.95, 0.001):
        parameters = []
        for ia in initial_as:
            parameters.append(PRLadapt(steps = n, initial_x = icx, initial_a = ia, r = randomness, max_x = 1.0, max_a = 4.0, N=2))

        plot_time_series(parameters, title = 'initial x == ' + str(icx))

# -----------------------------
