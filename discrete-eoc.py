import random
#from decimal import *

#getcontext().prec = 15

x_ = 0.38
#x_ = Decimal(0.380) + Decimal(0.0)
x = [x_]

a_ = 3.8
#a_ = Decimal(3.800)
a = [a_]

r = 0.0#0.005

#if a_ > 0:
#    a = [a_]
#else:
#    a = [3.8]

for n in range(100):
    print "----------"
#    print "0: a == ", a
    print "1: x_ == ", x_

    f = x_
    print "2: f == ", f
    for k in range(1, 33):
        x_ = a[n] * x_ * (1.0 - x_)
#        x_ = a[n] * x_ * (Decimal(1.0) - x_)
        print "m: x_ == ", x_
    
#    x_ = x_ + (random.random() - 0.5) * r
#    x_ = x_ + Decimal((random.random() - 0.5) * r)

    print "3: x_ == ", x_

    if x > 1:
        x_ = 0.999
#        x_ = Decimal(0.999)
    if x < 0:
        x = 0.001
#        x = Decimal(0.001)

    f = f - x_
    x.append(x_)
    a.append(a[n] + 0.1 * f)
#    a.append(a[n] + Decimal(0.1) * f)

    if a[n+1] < 0:
        a[n+1] = 0.0
#        a[n+1] = Decimal(0)
    
    if a[n+1] > 4:
        a[n+1] = 4.0
#        a[n+1] = Decimal(4)

    for k in range(1, 33):
        x_ = a[n] * x_ * (1.0 - x_)

print a


import matplotlib
import matplotlib.pyplot as plt

ax = plt.gca()
ax.ticklabel_format(useOffset=False)
plt.plot(a)
plt.grid()
plt.show()
