import matplotlib.pyplot as plt
import numpy as np

# Plotting sine and cosine with Matplotlib and Python
def plotsincos(st, sp, ic):
    x = np.arange(st, sp * np.pi, ic)
    y = np.sin(x)
    z = np.cos(x)

    plt.plot(x, y, x, z)
    plt.xlabel("x values from 0 to 4pi")  # string must be enclosed with quotes '  '
    plt.ylabel("sin(x) and cos(x)")
    plt.title("Plot of sin and cos from 0 to 4pi")
    plt.legend(["sin(x)", "cos(x)"])  # legend entries as seperate strings in a list
    plt.show()


plotsincos(0, 4, 0.1)
