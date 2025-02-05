import pandas as pd



print("\n\n------------------ 1.填充缺失值 ------------------------")
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, None, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
print("源数据：")
print(df)

# 填充缺失的 "Age" 为均值
df.loc[:, 'Age'].fillna(df.loc[:, 'Age'].mean(), inplace=True)
print('\n填充缺失的 "Age" 为均值:')
print(df)




print("\n\n------------------ 2.独热编码 ------------------------")
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("源数据：")
print(df,"\n")

print('对 "City" 列进行 One-Hot 编码:')
df_encoded = pd.get_dummies(df, columns=['City'],dtype=int)     # dtype=int:显示0或1，如果没有这个参数将显示true与false
print(df_encoded)



print("\n\n------------------ 3.标准化 ------------------------")
from sklearn.preprocessing import StandardScaler
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)
# 实例化StandardScaler对象，用于后续的数据标准化
scaler = StandardScaler()
# 应用fit_transform方法到DataFrame上，该方法会计算特征的平均值与标准差并据此对数据进行标准化
# 注意：fit_transform返回的是一个numpy数组，而不是DataFrame
df_scaled = scaler.fit_transform(df)
print(df_scaled)




# ========================== 完 ===========================