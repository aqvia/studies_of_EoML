import numpy as np
import matplotlib.pyplot as plt

def cointoss(n, m):
    l = []
    for _ in range(m):
        r = np.random.randint(2, size=n)
        l.append(r.sum())
    return l

np.random.seed(0)
fig, axes = plt.subplots(1, 2)

l = cointoss(100, 1000000)
axes[0].hist(l, range=(30, 70), bins=50, color="k")

l = cointoss(10000, 1000000)
axes[1].hist(l, range=(4800, 5200), bins=50, color="k")

plt.show()