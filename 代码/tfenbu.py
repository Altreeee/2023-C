#拟合t分布
import numpy as np
from scipy.stats import t

# 数据点
x = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
y = np.array([31, 272, 985, 1437, 1067, 563])

# 计算均值和标准差
x_mean = np.mean(x)
y_mean = np.mean(y)
x_std = np.std(x, ddof=1)
y_std = np.std(y, ddof=1)

# 计算t统计量
t_statistic = (y_mean - 1000) / (y_std / np.sqrt(len(y)))

# 计算自由度
df = len(y) - 1

# 计算显著性水平
p_value = t.sf(np.abs(t_statistic), df) * 2

print("t统计量为：", t_statistic)
print("自由度为：", df)
print("显著性水平为：", p_value)
