# Pandas essentials

# load librries
import numpy as np
import pandas as pd

# series
data = np.arange(1,100)
print(data)
df = pd.Series(data)
print(df)

import string
new_dict = {}
ascii = string.ascii_letters
for i, j in zip(range(52), ascii):
    new_dict[i] = j

print(new_dict)
s = pd.Series(new_dict)
print(s)

df = pd.Series([1,2,3,4,5,6,7], index=['a','s','d','f','g','h','j'])
print(df[:3], df['a'])

a = [1,2,3,4,5]
df = pd.DataFrame(a)
print(df)

d = [['Alex', 12], ['John', 32], ['Sam', 21], ['George', 33]]
df = pd.DataFrame(d, columns=['Name', 'Age'])
print(df)

d = {'a':1, 'b': 2, 'c':3, 'd':4, 'c':5}
df = pd.DataFrame(d, columns=['alphabet', 'numbers'])
print(df)

d = {'one': pd.Series([1,2,3], index=['a','b', 'c']),
     'two': pd.Series([4,5,6,7], index=['a', 'b', 'c', 'd'])}
s = pd.Series([1,2,3,4,5,6], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame(d)
df['three'] = pd.DataFrame(s, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(df)

del df['three']
print(df)

a = df.pop('two')
print(df, a)

# addition of rows 
df1 = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5,6], [7,8]], columns=['a', 'b'])
df1 = df1.append(df2)
print(df1[2:])

df1 = df1.drop(0)
print(df1)

#d = np.random.rand(2,4,5)
#p = pd.Panel(d)
#print(p)

# dataframe frunctionality
d = {'name': pd.Series(['Anna', 'George', 'Sam', 'Susan', 'Cloe']),
     'age': pd.Series([12, 34, 45, 54, 66, 23]),
     'salary': pd.Series([332, 432, 678, 654, 1001, 3214])}

df = pd.DataFrame(d)
print(df)

print(df.sum())
print(df.sum(1))

def adder(item1, item2):
    return item1+item2


d = pd.DataFrame(np.random.rand(5,3), columns=['r1', 'r2', 'r3'])
print(d)
d.pipe(adder, 2)
d.apply(np.mean)
print(d)

d['r1'].map(lambda x: x*100)
print("our result: ", d.apply(np.mean))

d = pd.DataFrame(np.random.rand(16,6), columns=['q','w','e','r','t','y'])
for k, v in d.iteritems():
    print("Our collumn is: {}, and row is: {}".format(k, v))

for r, rv in d.iterrows():
    print(r, rv)

# sortinf dtaframes
d = pd.DataFrame(np.random.rand(10, 2), index=[10,9,5,6,4,3,2,1,7,8], columns=['c2', 'c1'])
print(d)

s_d = d.sort_index()
print(s_d)

s_d = d.sort_index(axis=1)
print(s_d)

s_d = d.sort_values(by='c2')
print(s_d)

d = pd.DataFrame(np.random.rand(6,4), index=['a','b','c','d','e','f'], columns=['A','B','C','D'])
print(d)
print(d.loc[:,'A'])
print(d.loc[:, ['A', 'B']])

print(d.loc[['a','b','c','d'], ['C','D']])

print(d.loc['a':'c'])


d = pd.DataFrame(np.random.rand(8,4), columns=['a','b','c','d'])
print(d.iloc[:4,2:4])
print(d['a'])
print(d.a)

d = pd.DataFrame(np.random.rand(6,4), index=['a','c','f','h','l','n'], columns=['A','B','C','D'])
n_d = d.reindex(['a','b','c','d','e','f','g'])
print(n_d)
print(n_d['A'].isnull())
print(n_d.loc['a'].isnull())


print(n_d.fillna(777))
print(n_d.dropna())

d = pd.DataFrame({'age': [12,13,23,45], 'salary':[123,456,678,908]})
print(d.replace({45:1000, 908:2000}))

# grouping data

d = pd.DataFrame({'name': ['cings', 'bonor', 'aword'],
                  'rank': [1,3,2],
                  'year': [1989, 1993, 1997]})
print(d)
print(d.groupby('name').groups)

# merging data
left = pd.DataFrame({'id': [1,2,3],
                     'name': ['Anna', 'Adam', 'Alisa'],
                     'result': [78, 85, 48],
                     'grade': ['B', 'A', 'F']})
right = pd.DataFrame({'id': [1,2,3],
                      'name': ['Boris', 'Bran', 'Benjamin'],
                      'result': [91, 100, 55],
                      'grade': ['A', 'A+', 'F']})
data_merged = pd.merge(left, right, on='id')
print(data_merged)

data_concatenated = pd.concat([left, right], axis=1)
print(data_concatenated)

data_appended = left.append([right, left, right])
print(data_appended)

# pandas data tools
my_data = pd.date_range('1/1/2022', periods=5, freq='M')
print(my_data)

