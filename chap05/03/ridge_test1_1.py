import ridge
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
model = ridge.RidgeRegression(1.)
model.fit(x, y)
b, a = model.w_

plt.scatter(x, y, color="k")
xmax = x.max()
plt.plot([0, xmax], [b, b + a * xmax], color="k")
plt.show()
