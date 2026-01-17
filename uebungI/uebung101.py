import matplotlib.pyplot as plt

import numpy as np

def f1(x):
    return 1 + 3*x

def f2(x, a, b):
    return a + b*x

A = 0
B = 1
def f3(x, a=A, b=B):
    return a + b*x

def f4(x, *a):
    s = 0
    for i in range(len(a)):
        s += a[i] * (x**i)
    return s

def main():
    x = np.arange(0, 10, 0.1)

    plt.plot(x, f1(x))
    plt.plot(x, f2(x,2,3))
    plt.plot(x, f3(x))
    plt.plot(x, f4(x,0,1,3,0,0,7))

    plt.show()

if __name__ == "__main__":
    main()
