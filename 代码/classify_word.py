#将单词按照比例为正态分布来进行难度分类
import pandas as pd
import numpy as np
from scipy.stats import norm

# 读取Excel文件
df = pd.read_excel("data.xlsx")
difficulties = df["difficulty"]
words = df["word"]
n_words = len(words)

# 计算平均难度和方差
mean_difficulty = np.mean(difficulties)
var_difficulty = 1.47

# 创建正态分布对象
dist = norm(loc=mean_difficulty, scale=np.sqrt(var_difficulty))

# 计算每个难度区间的概率密度积分之比
intervals = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, np.inf)]
int_probs = []
for a, b in intervals:
    int_prob = dist.cdf(b) - dist.cdf(a)
    int_probs.append(int_prob)
int_probs = np.array(int_probs)
int_probs /= np.sum(int_probs)

# 生成符合正态分布的随机数
n_samples = 360
word_counts = np.zeros(7, dtype=int)
for i, (a, b) in enumerate(intervals):
    center = (a + b) / 2
    std = (b - a) / 6
    '''samples = np.round(np.random.normal(center, std, int(n_samples * int_probs[i])))
    counts = np.bincount(samples.astype(int))'''
    samples = np.round(np.random.normal(center, std, int(n_samples * int_probs[i]))).astype(int)
    samples = samples[samples >= 0]
    counts = np.bincount(samples)

    counts = np.append(counts, np.zeros(n_samples - len(counts), dtype=int))
    word_counts[i] = counts.sum()

# 配对单词和难度
word_indices = np.arange(n_words)
word_indices = np.random.permutation(word_indices)
word_lists = np.split(word_indices, np.cumsum(word_counts[:-1]))
diff_intervals = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6+"]
diffs = []
words_by_diff = []
for i, word_list in enumerate(word_lists):
    diff_str = diff_intervals[i]
    diff_center = (intervals[i][0] + intervals[i][1]) / 2
    diffs += [diff_center] * len(word_list)
    words_by_diff.append([words[j] for j in word_list])

# 输出到Excel文件
output_data = {"difficulty": diffs, "word": [word for words in words_by_diff for word in words]}
output_df = pd.DataFrame(output_data)
output_df.to_excel("output.xlsx", index=False)
