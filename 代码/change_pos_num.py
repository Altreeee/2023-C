#将单词的不同词性使用字母代替
import pandas as pd

# 读取xlsx文件
df = pd.read_excel('word_pos.xlsx')

# 将每个词性映射到唯一的数字
pos_dict = {}
pos_count = 0
for pos in df['pos'].unique():
    pos_dict[pos] = pos_count
    pos_count += 1

# 将每个词性替换为对应的数字，并存入新的一列中
df['pos_num'] = df['pos'].map(pos_dict)

# 保存修改后的文件
df.to_excel('word_num.xlsx', index=False)
