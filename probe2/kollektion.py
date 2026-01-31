import matplotlib.pyplot as plt

import numpy as np

def l1():
    return [(i+1)**3 for i in range(-20,23,2)]

def l2() -> list[int]:
    return [(i**2+2) for i in range(-11,11,1)] #muss ändern, weil l1 nur 22 Elemente hat, weil l2 23 Elemente gibt

def d1() -> dict[int, int]:
    l = l1() + l2()
    return { i : l[i] for i in range(len(l))}

def plot():

    l1_achse = np.array(l1())
    l2_achse = np.array(l2())
    plt.plot(l1_achse,l2_achse ,color='red')
    plt.xlabel('l1')
    plt.ylabel('l2')
    plt.title('l')
    plt.show()

if __name__ == "__main__":
    plot()