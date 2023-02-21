#拟合指数分布
import numpy as np
from scipy.stats import expon,kstest

# 指数分布的参数
lamda = 0.5

# 创建一个指数分布对象
exponential_dist = expon(scale=1/lamda)

# 计算概率密度函数
x = np.linspace(0, 10, 100)
pdf = exponential_dist.pdf(x)

# 计算累积分布函数
cdf = exponential_dist.cdf(x)

# 生成随机样本
samples = exponential_dist.rvs(size=1000)

# 进行KS检验
ks_stat, p_value = kstest(samples, 'expon', args=(0, 1/lamda))

# 打印结果
print("KS检验统计量：", ks_stat)
print("p值：", p_value)

# 打印结果
print("概率密度函数：", pdf)
print("累积分布函数：", cdf)
print("前5个随机样本：", samples[:5])
