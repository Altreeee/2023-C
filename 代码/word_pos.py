#使用nltk库来对单词进行词性标注
import pandas as pd
import nltk

# 定义函数进行词性标注
def pos_tagging(word):
    pos = nltk.pos_tag([word])
    return pos[0][1]

# 读取原始xlsx文件
df = pd.read_excel('word.xlsx')

# 在DataFrame中添加新的一列，包含词性标注
df['pos'] = df.iloc[:,3].apply(pos_tagging)  # 假设文字列是第四列

# 将新的xlsx文件写入磁盘
df.to_excel('output.xlsx', index=False)
