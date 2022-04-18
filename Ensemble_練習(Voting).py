# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:58:16 2021

@author: sam60427
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('C:/Users/sam60427/Desktop/110年邊境專案/原始資料ABCD/其他A_新11.csv')
# 將類別與數值型變數分組
num_list = []
category = []
for i in data.columns:
    if data[i].dtype == 'int64' or data[i].dtype == 'float64':
        if '是否' not in i:
            num_list.append(i)
        else:
            category.append(i)
    else:
        category.append(i)
le = LabelEncoder()
for ii in category:
    data[ii] = le.fit_transform(data[ii].astype(str))
y = data['class']
x = data.drop(['class', '簽審核准許可文件編號', '報驗義務人統一編號', '報單號碼', '報單項次', '檢驗不合格'], axis=1)
y = le.fit_transform(y)
# 訓練組與測試組
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# 決策樹模型
clf_tree = DecisionTreeClassifier(criterion='gini', max_depth=10)
# 隨機森林模型
clf_rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=50, min_samples_leaf=10)
# 樸素貝葉斯
clf_nb = GaussianNB()
# 將子模型存入
model_list = []
model_list.append(('決策樹', clf_tree))
model_list.append(('隨機森林', clf_rfc))
model_list.append(('樸素貝葉斯', clf_nb))
# 使用 Voting 將這些”不同類型”的弱學習器結合在一起
# VotingClassifier 適合用在分類問題，VotingRegressor 則適合用在連續型資料
clf_vc = VotingClassifier(model_list)
model_vc = clf_vc.fit(x_train, y_train)
pre_result = model_vc.predict(x_test)
# {:%} 代表顯示百分比樣式
print('使用 VotingClassifier 方法預測之準確率為：{:%}'.format(model_vc.score(x_test, y_test)))
