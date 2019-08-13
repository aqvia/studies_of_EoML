import ridge
import sys
sys.path.append('../02')
import linearreg
import numpy as np
import matplotlib.pyplot as plt

# ほぼ線形だが、2つだけ大きくずれたデータ
x = np.arange(12)
y = 1 + 2 * x
y[2] = 20
y[4] = 0

xmin = 0
xmax = 12
ymin = -1
ymax = 25
fig, axes = plt.subplots(nrows=2, ncols=5)

for i in range(5):
    axes[0, i].set_xlim([xmin, xmax])
    axes[0, i].set_ylim([ymin, ymax])
    axes[1, i].set_xlim([xmin, xmax])
    axes[1, i].set_ylim([ymin, ymax])
    # データを2個から2個ずつ増やしていく
    xx = x[:2 + i * 2]
    yy = y[:2 + i * 2]
    axes[0, i].scatter(xx, yy, color="k")
    axes[1, i].scatter(xx, yy, color="k")
    # (上)線形回帰
    model = linearreg.LinearRegression()
    model.fit(xx, yy)
    xs = [xmin, xmax]
    ys = [model.w_[0] + model.w_[1] * xmin, model.w_[0] + model.w_[1] * xmax]
    axes[0, i].plot(xs, ys, color="k")
    # (下)Ridge回帰
    model = ridge.RidgeRegression(10.)
    model.fit(xx, yy)
    xs = [xmin, xmax]
    ys = [model.w_[0] + model.w_[1] * xmin, model.w_[0] + model.w_[1] * xmax]
    axes[1, i].plot(xs, ys, color="k")

plt.show()