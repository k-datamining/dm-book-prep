#!/usr/bin/env python
# coding: utf-8

# # テーブルの列を列名のパターンマッチで選択
# ## サンプルデータ

# In[1]:


import pandas as pd

X = pd.read_csv("../../data/sample.csv")
X.head()


# ## sklearn.compose.make_column_selector
# [sklearn.compose.make_column_selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html)
# を使用します。`pattern="暦"`で暦が含まれる列を選択し、StandardScalerを適用します。

# In[2]:


from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector

n_ss = StandardScaler()

# 暦が含まれる列のみスケーリング
ct = make_column_transformer(
    (n_ss, make_column_selector(pattern="暦")), sparse_threshold=0
)
X_transform = ct.fit_transform(X)

# 変換後のテーブル
pd.DataFrame(X_transform).head()

