#计算eerie的分布曲线
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 读取Excel表格
df = pd.read_excel('tries_46.xlsx')

# 定义正态分布函数
def normal(x, mu, sigma, A):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

# 遍历前7列数据
mean_vars = []
for i, row in df.iloc[:, :7].iterrows():
    x = np.array([1, 2, 3, 4, 5, 6]) # 游戏难度的取值
    y = np.array(row[0:6])         # 当天每个难度的完成人数

    # 使用 curve_fit 函数拟合正态分布曲线
    popt, pcov = curve_fit(normal, x, y, p0=[3, 1, 100])
    mu, sigma, A = popt

    # 计算均值处的x值
    mu_x = mu # x的取值是 1~6，需要将均值点的x值加1
    print('Day {}: mean difficulty = {:.2f}'.format(i+1, mu_x))

    # 将均值处的x值插入数据表中
    df.loc[i, 'mean_difficulty'] = mu_x

    # 计算残差平方和
    rss = np.sum((y - normal(x, *popt))**2)
    # 将残差平方和插入数据表中
    df.loc[i, 'residual_sum_of_squares'] = rss

    # 将方差插入列表中
    mean_vars.append(sigma ** 2)

# 计算所有方差的平均值
mean_var = np.mean(mean_vars)
'''mean_var = 1.3'''
print(mean_var)

# 计算新的正态分布曲线

new_mu = 4.496  #15000
'''new_mu = 4.4985  # 均值
new_mu = 4.507  #10000
'''
new_sigma = np.sqrt(mean_var)  # 标准差


new_y = normal(x, new_mu, new_sigma, A)

# 可视化新的正态分布曲线
x_new = np.array([1, 2, 3, 4, 5, 6])
y_new = normal(x_new, new_mu, new_sigma, A)
plt.plot(x_new, y_new)
plt.xlabel('Game difficulty')
plt.ylabel('Number of completions')
plt.title('New Normal Distribution')
plt.show()

# 计算新的正态分布曲线在 x=1,2,3,4,5,6 时的值
for i in range(len(x_new)):
    print('x={}时，y={:.2f}'.format(x_new[i], y_new[i]))

# 将数据表保存为新的Excel文件
'''df.to_excel('result.xlsx', index=False)'''
