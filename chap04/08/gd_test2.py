import numpy as np
import matplotlib.pyplot as plt
import gd

# 関数の定義
def f(xx):
    x = xx[0]
    y = xx[1]
    return 5 * x**2 - 6 * x * y + 3 * y**2 + 6 * x - 6 * y

# 導関数の定義
def df(xx):
    x = xx[0]
    y = xx[1]
    return np.array([10 * x - 6 * y + 6, -6 * x + 6 * y - 6])

# 最適化の計算
algos = []
alphas = [0.1, 0.05]
initial = np.array([1, 1])
for alpha in alphas:
    algo = gd.GradientDescent(f, df, alpha)
    algo.solve(initial)
    algos.append(algo)

# 図の描画
# 等高線
xmin, xmax, ymin, ymax = -3, 3, -3, 3
xs = np.linspace(xmin, xmax, 300)
ys = np.linspace(ymin, ymax, 300)
xmesh, ymesh = np.meshgrid(xs, ys)
xx = np.r_[xmesh.reshape(1, -1), ymesh.reshape(1, -1)]
fig, ax = plt.subplots(1, 2)
levels = [-3, -2.9, -2.8, -2.6, -2.4, -2.2, -2, -1, 0, 1, 2, 3, 4]
for i in range(2):
    ax[i].set_xlim((xmin, xmax))
    ax[i].set_ylim((ymin, ymax))
    ax[i].set_title("alpha={}".format(alphas[i]))
    # 始点
    ax[i].scatter(initial[0], initial[1], color="k", marker="o")
    # 収束までの点の軌跡
    ax[i].plot(algos[i].path_[:, 0], algos[i].path_[:,1], color="k", linewidth=1.5)
    ax[i].contour(xs, ys, f(xx).reshape(xmesh.shape), levels=levels, colors="k", linestyles="dotted")

plt.show()
