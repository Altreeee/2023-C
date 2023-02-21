#统计单词中字母出现的次数
import pandas as pd

# 读取xlsx文件
df = pd.read_excel('word.xlsx')

# 新建一列来存放每个单词中'e'出现的次数
df['an_count'] = 0

# 遍历第三列中的每个单词，计算'e'出现的次数，并将其存入新的一列
for index, row in df.iterrows():
    word = str(row[2])  # 获取第三列中的单词
    e_count = word.count('an')  # 计算'e'出现的次数
    df.at[index, 'an_count'] = e_count  # 存入新的一列中

# 保存修改后的文件
df.to_excel('an.xlsx', index=False)
