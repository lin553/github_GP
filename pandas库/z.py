import numpy as np
import pandas as pd

a = np.random.randint(0,10,(3,3))
print(a)

print('\n----------------------------')
b = np.linspace(0,3,100)
print(b)

print('\n----------------------------')
c = np.eye(100)
print(c)

print('\n----------------------------')
print(c[:10])


print('\n-----------向量化运算-----------------')
a = pd.Series([1,2,3,4],index=['a', 'b', 'c','d'])
b = pd.Series([2,3,4,5],index=['a', 'e', 'f', 'g'])

print('a:\n',a,'\n\nb:\n',b)
c = a + b
print('\nc: \n',c)

c.dropna()
print('\nc.dropna(): \n',c)

c = a.add(b, fill_value=0)
print('\na.add(b, fill_value=0): \n',c)