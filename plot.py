import matplotlib.pyplot as plt

with open('param-values.txt', 'rU') as in_file:
    data = in_file.read().split(',')

    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)
    plt.plot(data)
    plt.grid()
    plt.show()
