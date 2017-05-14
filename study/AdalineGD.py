# -*- coding: utf-8 -*-
import numpy as np
class AdalineGD(object):
    """ADAptive Linear NEuron 分類器
    
    パラメータ
    -------------
    eta : float
        学習率　(0.0 < η <= 1.0)
    n_iter : int 
        トレーニングデータのトレーニング回数
    
    属性
    -------------
    w_ : 1次元配列
    　　適合後の重み
    errors_ : リスト
    　　各エポックでの誤分類数
    """
    
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        
    def fit(self, X, y):
        """トレーニングデータに適合させる
        
        パラメータ
        ---------------
        X : { 配列のようなデータ構造 } , shape = {n_samples, n_features}
            トレーニングデータ
            n_samplesは配列の個数, n_featuresは特徴量の個数
        y : 配列のようなデータ構造, shape = [n_samples]
            目的変数
            
        戻り値
        -------------
        self : object
        
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum()/2.0
            self.cost_.append(cost)
        return self
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return self.net_input(X)
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    