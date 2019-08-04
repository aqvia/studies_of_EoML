import linearreg
import numpy as np
import csv

# データの読み込み
Xy = []
with open("winequality-red.csv") as fp:
    for row in csv.reader(fp, delimiter=";"):
        Xy.append(row)
# 1行目は読み飛ばす
Xy = np.array(Xy[1:], dtype=np.float64)

# ホールド・アウト検証(Holdout method)
# 訓練データとテストデータに分割
np.random.seed(0)
np.random.shuffle(Xy)
train_X = Xy[:-1000, :-1]
train_y = Xy[:-1000, -1]
test_X = Xy[-1000:, :-1]
test_y = Xy[-1000:, -1]

# 学習
model = linearreg.LinearRegression()
model.fit(train_X, train_y)

# テストデータにモデルを適用
y = model.predict(test_X)

print("最初の5つの正解 予測値:")
for i in range(5):
    print("{:1.0f} {:5.3f}".format(test_y[i], y[i]))
print()
# 予測の評価値
# RMSE = Root of Mean Squear Error をとる
# 1未満なのでまあまあ
print("RMSE: ", np.sqrt(((test_y - y)**2).mean()))