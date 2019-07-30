import linearreg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# 入力データ生成: 2次元
n = 100 # サンプル数
scale = 10
np.random.seed(0)
X = np.random.random((n, 2)) * scale

# 出力データ生成
w0 = 1
w1 = 2
w2 = 3
y = w0 + w1 * X[:, 0] + w2 * X[:, 1] + np.random.randn(n)

model = linearreg.LinearRegression()
model.fit(X, y)
print("係数:", model.w_)
# 真の値は [1, 2, 3]。それに近いか?
print("(1,1)に対する予測値:", model.predict(np.array([1, 1])))
# 真の値は 1+2*1+3*1 = 6。それに近いか?

# 可視化: 3次元
xmesh, ymesh = np.meshgrid(np.linspace(0, scale, 20), np.linspace(0, scale, 20))
zmesh = (model.w_[0] + model.w_[1] * xmesh.ravel() + model.w_[2] * ymesh.ravel()).reshape(xmesh.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y, color="r")
ax.plot_wireframe(xmesh, ymesh, zmesh, color="r")
plt.show()