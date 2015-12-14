import random

x_ = 0.38
x = [0.38]

a_ = 3.8

r = 0.0#0.005

if a_ > 0:
    a = [a_]
else:
    a = [3.8]

for n in range(10):
    print "----------"
    print "x_ == ", x_

    f = x_
    print "f == ", f
    for k in range(1, 33):
        x_ = a[n] * x_ * (1 - x_)
        print "x_ == ", x_
    
    x_ = x_ + (random.random() - 0.5) * r

    print "x_ == ", x_

    if x > 1:
        x_ = 0.999
    if x < 0:
        x = 0.001

    f = f - x_
    x.append(x_)
    a.append(a[n] + 0.1 * f)

    if a[n+1] < 0:
        a[n+1] = 0
    
    if a[n+1] > 4:
        a[n+1] = 4

    for k in range(1, 33):
        x_ = a[n] * x_ * (1 - x_)

print a
