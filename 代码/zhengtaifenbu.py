#拟合正态分布
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, kstest

plt.clf()  # 清空图像

# 已知数据点
x = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
y = [31, 272, 985, 1437, 1067, 563]

# 使用最大似然估计法估计正态分布的参数
mean = sum([x[i] * y[i] for i in range(len(x))]) / sum(y)
variance = sum([(x[i]-mean)**2 * y[i] for i in range(len(x))]) / sum(y)

# 绘制正态分布的概率密度函数
x_axis = np.linspace(min(x), max(x), 1000)
y_axis = norm.pdf(x_axis, mean, np.sqrt(variance))
plt.plot(x_axis, y_axis)

# 进行KS检验
ks_statistic, p_value = kstest(x, 'norm', args=(mean, np.sqrt(variance)))

# 打印检验结果
print('KS statistic: ', ks_statistic)
print('p-value: ', p_value)


'''
# 设置y轴上下限
plt.ylim(0, max(max(y), max(y_axis)) * 1.1)
# 添加柱状图
plt.bar(x, y, width=0.5)


'''
# 显示图像
plt.show()



