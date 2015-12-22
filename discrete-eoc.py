import random
#from decimal import *

#getcontext().prec = 15

x_ = 0.38
#x_ = Decimal(0.380) + Decimal(0.0)
#x = [x_]
x = []

a_ = 3.8
#a_ = 2.1
#a_ = Decimal(3.800)
a = [a_]

r = 0#0.005

for n in range(1000):
    #print "----------"
#    print "0: a == ", a
    #print "1: x_ == ", x_

    f = x_
    #print "2: f == ", f
    #print ": a[n] == ", a[n]
    for k in range(1, 33):
        x_ = a[n] * x_ * (1.0 - x_)
#        x_ = a[n] * x_ * (Decimal(1.0) - x_)
#        print "m: x_ == ", x_
    
#    x_ = x_ + (random.random() - 0.5) * r
#    x_ = x_ + Decimal((random.random() - 0.5) * r)

    #print "3: x_ == ", x_

    if x_ > 1:
        x_ = 0.999
#        x_ = Decimal(0.999)
    if x_ < 0:
        x_ = 0.001
#        x = Decimal(0.001)

    f = f - x_

    #print "4: f == ", f
    #print "5: a as list == ", a
    #print "6: x as list == ", x

#    print ": f == ", f
#
#    print "len(x): ", len(x)
#    print "len(a): ", len(a)
#    print "n: ", n

    #print ": a[n] == ", a[n]

    x.append(x_)
#    x[n-1] = x_
    a.append(a[n] + 0.1 * f)
#    a.append(a[n] + Decimal(0.1) * f)

    #print "7: a as list == ", a
    #print "8: x as list == ", x

    #print "9: a[n] == ", a[n]
    #print "10: a[n+1] == ", a[n+1]

    if a[n+1] < 0:
        a[n+1] = 0.0
#        a[n+1] = Decimal(0)
    
    if a[n+1] > 4:
        a[n+1] = 4.0
#        a[n+1] = Decimal(4)

    for k in range(1, 32):
        x_ = a[n] * x_ * (1.0 - x_)

print a


import matplotlib
import matplotlib.pyplot as plt

ax = plt.gca()
ax.ticklabel_format(useOffset=False)
plt.plot(a)
plt.grid()
plt.show()
