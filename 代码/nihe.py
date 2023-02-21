#给每一个单词都拟合一条正态分布曲线
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
for i, row in df.iloc[:, :7].iterrows():
    x = np.array([1, 2, 3, 4, 5, 6]) # 游戏难度的取值
    y = np.array(row[0:6])         # 当天每个难度的完成人数

    # 使用 curve_fit 函数拟合正态分布曲线
    popt, pcov = curve_fit(normal, x, y, p0=[3, 1, 100])
    mu, sigma, A = popt

    '''# 可视化正态分布曲线
    x_plot = np.linspace(1, 6, 1000)
    y_plot = normal(x_plot, mu, sigma, A)
    plt.plot(x, y, 'o', label='data')
    plt.plot(x_plot, y_plot, label='fit')
    plt.xlabel('Game difficulty')
    plt.ylabel('Number of completions')
    title = row[6] # 获取每行的第7列作为标题
    plt.title(title)
    plt.legend()
    plt.show()'''

    # 计算均值处的x值
    mu_x = mu + 1 # x的取值是 1~6，需要将均值点的x值加1
    print('Day {}: mean difficulty = {:.2f}'.format(i+1, mu_x))

    # 将均值处的x值插入数据表中
    df.loc[i, 'mean_difficulty'] = mu_x

    # 计算残差平方和
    rss = np.sum((y - normal(x, *popt))**2)
    # 将残差平方和插入数据表中
    df.loc[i, 'residual_sum_of_squares'] = rss


# 将数据表保存为新的Excel文件
df.to_excel('result_1.xlsx', index=False)
