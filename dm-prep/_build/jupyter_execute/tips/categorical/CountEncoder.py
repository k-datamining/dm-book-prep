#!/usr/bin/env python
# coding: utf-8

# # CountEncoder
# 
# ## サンプルデータ
# 「人口総数」を予測したいとして、「元号」をエンコードしたいとします。

# In[1]:


import pandas as pd

X = pd.read_csv("../../data/sample.csv")
TARGET_NAME = "人口総数"
FEATURE_NAME = "元号"
X.head()


# ## CountEncoder
# - [category_encoders.count.CountEncoder](http://contrib.scikit-learn.org/category_encoders/count.html)
# 
# を使用します。

# In[2]:


from category_encoders.count import CountEncoder
from sklearn.compose import make_column_transformer

c_ce = CountEncoder()

y = X[TARGET_NAME]
X[f"{FEATURE_NAME}_ce"] = c_ce.fit_transform(X[FEATURE_NAME], y)


# ## 結果を確認する
# カテゴリ変数の列が `CountEncoder` でエンコードされていることを確認します。

# In[3]:


X[[FEATURE_NAME, f"{FEATURE_NAME}_ce"]]


# ## 元号の出現回数を確認する

# In[4]:


X[FEATURE_NAME].value_counts()

