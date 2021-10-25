#!/usr/bin/env python
# coding: utf-8

# # Target Encoder
# 
# ## サンプルデータ
# 「人口総数」を予測したいとして、「元号」をエンコードしたいとします。

# In[1]:


import pandas as pd

X = pd.read_csv("../../data/sample.csv")
TARGET_NAME = "人口総数"
FEATURE_NAME = "元号"
X.head()


# ## TargetEncoder
# - [category_encoders.target_encoder.TargetEncoder](http://contrib.scikit-learn.org/category_encoders/targetencoder.html)
# - [sklearn.compose.make_column_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)
# 
# を使用します。

# In[2]:


from category_encoders.target_encoder import TargetEncoder

c_te = TargetEncoder()

y = X[TARGET_NAME]
X[f"{FEATURE_NAME}_te"] = c_te.fit_transform(X[FEATURE_NAME], y)


# ## 結果を確認する
# カテゴリ変数の列が `TargetEncoder` でエンコードされていることを確認します。
# この方法は、目的変数の平均値をそのままエンコードに使用します。つまり、あるデータをエンコードするために**そのデータの目的変数の情報**を使用しています(leakage[1]と呼びます)。そのため、データ数が少ない場合は特に、実際に将来のデータに対して予測した場合とCVで評価した場合を比較すると、CV時に誤差が少なく見積もられる可能性がある点に注意して下さい。
# 
# [1] Kaufman, Shachar, et al. "Leakage in data mining: Formulation, detection, and avoidance." ACM Transactions on Knowledge Discovery from Data (TKDD) 6.4 (2012): 1-21.

# In[3]:


X[[FEATURE_NAME, f"{FEATURE_NAME}_te"]]


# ## 元号ごとの平均値
# 元号ごとのターゲットの平均値を用いてエンコードされていることを確認します

# In[4]:


X.groupby(FEATURE_NAME).agg("mean")[TARGET_NAME]

