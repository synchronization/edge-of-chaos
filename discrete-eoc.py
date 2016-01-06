#!/usr/local/bin/python2.7

__author__ = "Roozbeh Daneshvar"
__email__ = "roozbeh.daneshvar@gmail.com"

import random

# -----------------------------

def tent_map_function(x, a):
#    print 'x: ', x, '\ta: ', a
    return a * min(x, 1 - x)

# -----------------------------

def logistic_map_function(x, a):
    return a * x * (1.0 - x)

# -----------------------------

def dynamics_function(x, a):
#    return logistic_map_function(x, a)
    return tent_map_function(x, a)

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
    import matplotlib
    import matplotlib.pyplot as plt

    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)
    for a in inputs:
        plt.plot(a)
    plt.grid()
    plt.show()

# -----------------------------

#a1 = iterations(steps = 1000, r = 0.0)
#a2 = iterations(steps = 1000, r = 0.005)

n = 2000

a = []
a.append(iterations(steps = n, initial_x = 0.38, initial_a = 1.9, r = 0.0005))
a.append(iterations(steps = n, initial_x = 0.38, initial_a = 1.8, r = 0.0005))
a.append(iterations(steps = n, initial_x = 0.38, initial_a = 1.7, r = 0.0005))
a.append(iterations(steps = n, initial_x = 0.38, initial_a = 1.6, r = 0.0005))
a.append(iterations(steps = n, initial_x = 0.38, initial_a = 1.5, r = 0.0005))
a.append(iterations(steps = n, initial_x = 0.38, initial_a = 1.4, r = 0.0005))

plot_parameters(a)

# -----------------------------
