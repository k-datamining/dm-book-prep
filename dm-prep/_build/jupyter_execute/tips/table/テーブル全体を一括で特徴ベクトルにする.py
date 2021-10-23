#!/usr/bin/env python
# coding: utf-8

# # テーブル全体を一括で特徴ベクトルにする
# ## サンプルデータ

# In[1]:


import pandas as pd

X = pd.read_csv("../../data/sample.csv")
X.head()


# ## make_column_transformer
# [sklearn.compose.make_column_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)
# を使用します。

# In[2]:


from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer

c_oh = OneHotEncoder()
n_ss = StandardScaler()

ct = make_column_transformer(
    (c_oh, ["元号", "町名"]),  # カテゴリ変数にonehot
    (n_ss, ["西暦", "人口総数"]),  # 数値列をスケーリング
    remainder="passthrough",  # 指定の無い列はそのまま
    sparse_threshold=0,
)

X_transform = ct.fit_transform(X)

# 変換後のテーブル
pd.DataFrame(X_transform).head()

