#!/usr/bin/env python
# coding: utf-8

# # One-hot
# ## サンプルデータ

# In[1]:


import pandas as pd

X = pd.read_csv("../../data/sample.csv")
X.head()


# ## OneHotEncoder
# - [sklearn.preprocessing.OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
# - [sklearn.compose.make_column_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)
# を使用します。

# In[2]:


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

c_oh = OneHotEncoder()

ct = make_column_transformer(
    (c_oh, ["元号"]),  # カテゴリ変数にonehotを適用するように指定
    sparse_threshold=0,  # 結果の行列をdenseな行列にする
)


# ## 結果を確認する
# 元号（大正・昭和・平成）が三次元のベクトルになっていることが確認できます。

# In[3]:


# 変換方法を求めて、変換した結果を返す
X_transform = ct.fit_transform(X)

# 変換後のテーブルを表示
pd.DataFrame(X_transform).head()

