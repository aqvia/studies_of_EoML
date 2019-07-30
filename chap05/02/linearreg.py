import numpy as np
from scipy import linalg

class LinearRegression:
    def __init__(self):
        self.w_ = None

    def fit(self, X, t):
        """
        訓練データによる学習
        self.w_に計算データが格納される

        Parameters
        ----------
        X: ndarray
            入力訓練データ
        t: ndarray
            出力訓練データ
        """
        Xtil = np.c_[np.ones(X.shape[0]), X]
        A = np.dot(Xtil.T, Xtil)
        b = np.dot(Xtil.T, t)
        self.w_ = linalg.solve(A, b)

    def predict(self, X):
        """
        入力値に対して出力値を予測

        Parameters
        ----------
        X: ndarray
            評価用データ
        
        Returns
        -------
        ndarray 予測値
        """
        if X.ndim == 1:
            X = X.reshape(1, -1)
        Xtil = np.c_[np.ones(X.shape[0]), X]
        return np.dot(Xtil, self.w_)
