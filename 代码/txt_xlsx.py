#将txt文件转为xlsx表格
import pandas as pd

# 读取txt文件
with open("word.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 将每行数据按照':'分割，并创建DataFrame
data = [line.strip().split(":") for line in lines]
df = pd.DataFrame(data, columns=["word", "pos"])

# 将DataFrame输出到Excel文件
df.to_excel("word_pos.xlsx", index=False)
