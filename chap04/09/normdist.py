import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-5, 5)
y = norm.pdf(x, loc=1, scale=2)
plt.plot(x, y, color="r")
plt.show()