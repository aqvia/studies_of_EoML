import numpy as np
import matplotlib.pyplot as plt

# 最小二乗法による、直線で近似した時の傾き
def reg1dim1(x, y):
    a = np.dot(x, y) / (x ** 2).sum()
    return a

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
a = reg1dim1(x, y)

plt.scatter(x, y, color="k")
xmax = x.max()
plt.plot([0, xmax], [0, a*xmax], color="k")
plt.show()