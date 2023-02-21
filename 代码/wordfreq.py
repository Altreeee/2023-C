#使用下载的词频列表给单词添加上词频
import pandas as pd

# 读取包含单词频率的Excel文件
freq_df = pd.read_excel("freq.xlsx")

# 读取需要添加频率的单词列表
words_df = pd.read_excel("word.xlsx")#header=None, names=["word"]

# 将两个表格按照单词合并
merged_df = pd.merge(words_df, freq_df, on="word", how="left")

# 将未匹配到的单词的频率填充为0
merged_df["freq"] = merged_df["freq"].fillna(0)

# 将结果输出到新的Excel文件
merged_df.to_excel("result.xlsx", index=False)
