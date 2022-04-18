# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:27:55 2022

@author: user1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

categories = pd.read_csv('C:/Users/user1/Desktop/Kaggle/item_categories.csv')
item = pd.read_csv('C:/Users/user1/Desktop/Kaggle/items.csv')
train = pd.read_csv('C:/Users/user1/Desktop/Kaggle/sales_train.csv')
submission = pd.read_csv('C:/Users/user1/Desktop/Kaggle/sample_submission.csv')
shops = pd.read_csv('C:/Users/user1/Desktop/Kaggle/shops.csv')
test = pd.read_csv('C:/Users/user1/Desktop/Kaggle/test.csv')
 

train.item_price.plot(kind='line', color='g', label='item_price',
                      linewidth=1, alpha=0.5, grid=True, linestyle=':')
plt.legend(loc='upper right')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line Plot')
#plt.show()

train[train['item_id'] > 22000]
train[(train['item_id'] > 22000) & (train['item_price'] > 1000)]
train[np.logical_and(train['item_id'] > 22000, train['item_price'] > 1000)]
# 按照金額新增欄位並給予高低分類
threshold = sum(train.item_price)/len(train.item_price)
train['item_price_level'] = ['high' if i > threshold else 'low' for i in train.item_price]
train.shape
train['item_price'].value_counts(dropna=False)

data1 = train.head()
data2 = train.tail()
data = pd.concat([data1, data2], axis=0, ignore_index=True)

test['item_id'] = test['item_id'].astype('category')
test['shop_id'] = test['shop_id'].astype('string')

shops.shape
shops['shop_name'].value_counts(dropna=False)
shops['shop_name'].dropna(inplace=True)
assert shops['shop_name'].notnull().all()

country = ['Spain', 'France']
population = ['11', '12']
list_label = ['country', 'population']
list_col = [country, population]
zipped = list(zip(list_label, list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
df['capital'] = ['madrid', 'pairs']
df.at[0, 'capital'] = 0

time_list = ['1992-03-08', '1992-04-12']
datetime = pd.to_datetime(time_list)
print(type(datetime))

data = item.set_index('item_id')
data['item_category_id'][40]
data.loc[0:10, 'shop_id':'item_cnt_day']
data.loc[1:10, 'item_price':]
n1 = train.item_price > 1000
n2 = train.shop_id == 25
train[n1 & n2]
train.shop_id[train.item_price < 1000]

def div(n):
    return n/2
train.item_price.apply(div)
train.item_price.apply(lambda n:n/2)
train['total_power'] = train.shop_id + train.item_id
train.index = range(100, 2935949, 1)
### STACKING and UNSTACKING DATAFRAME
dic = {'treatment':['A', 'A', 'B', 'B'], 
       'gender':['F', 'M', 'F', 'M'],
       'response':[10, 45, 5, 9],
       'age':[15, 4, 72, 65]}
df1 = pd.DataFrame(dic)
df1.pivot(index='treatment', columns='gender', values='response')
df2 = df1.set_index(['treatment', 'gender'])

import warnings
warnings.filterwarnings("ignore")
data2 = train.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
data2 = data2.set_index("date")

shops.set_index('shop_id', inplace=True)
train['shop_id'].nunique()
train['date'] = pd.to_datetime(train['date'])
# 日期轉換新增欄位
train['year'] = train['date'].dt.year
train['month'] = train['date'].dt.month

