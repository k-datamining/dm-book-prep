#!/usr/bin/env python
# coding: utf-8

# # Ordered Target Statistics
# 参考文献：Prokhorenkova, Liudmila, et al. "CatBoost: unbiased boosting with categorical features." arXiv preprint arXiv:1706.09516 (2017).
# 
# 
# ## サンプルデータ
# 「人口総数」を予測したいとして、「元号」をエンコードしたいとします。

# In[1]:


import pandas as pd

X = pd.read_csv("../../data/sample.csv")
TARGET_NAME = "人口総数"
FEATURE_NAME = "元号"
X.head()


# ## Ordered Target Statistics
# - [category_encoders.cat_boost.CatBoostEncoder](http://contrib.scikit-learn.org/category_encoders/catboost.html)
# - [sklearn.compose.make_column_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)
# 
# を使用します。

# In[2]:


from category_encoders.cat_boost import CatBoostEncoder
from sklearn.compose import make_column_transformer

c_ots = CatBoostEncoder()

y = X[TARGET_NAME]
X[f"{FEATURE_NAME}_ots"] = c_ots.fit_transform(X[FEATURE_NAME], y)


# ## 結果を確認する
# カテゴリ変数の列が `CatBoostEncoder` でエンコードされていることを確認します。

# In[3]:


X[[FEATURE_NAME, f"{FEATURE_NAME}_ots"]]


# ## エンコード結果の分布を確認する

# In[4]:


import matplotlib.pyplot as plt
import japanize_matplotlib

plt.figure(figsize=(8, 4))
for i, ci in enumerate(X[FEATURE_NAME].unique()):
    plt.hist(
        X.query(f"{FEATURE_NAME}=='{ci}'")[f"{FEATURE_NAME}_ots"], label=ci, alpha=0.5
    )

plt.title("エンコードされた結果の分布")
plt.legend(title=FEATURE_NAME)

