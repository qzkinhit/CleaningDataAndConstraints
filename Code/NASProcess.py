import pandas as pd
import random
import os

os.chdir(r"E:\ZMY\repairboth论文内容\实验\CleaningDataAndConstraints\Code") 

# min_lst = [49.34, 51.95, 44.31, 43.44, 35.15, 84.89]
# max_lst = [50.61, 53.13, 47.35, 79.43, 51.11, 132]

min_lst = [0.6, 0.3, 45, 2600, 100, 0.04, 0.14, 100, 0.04, 0.09]
max_lst = [0.7, 0.4, 46, 2700, 100, 0.05, 0.14, 100, 0.05, 0.09]

# for i in range(4):
#     print(min(data[i]),max(data[i]))
# print(data[0].iloc[:200].mean())
for j in range(1):
    # data = pd.read_csv("../DataSample/PUMP-10000-GroundTruth.csv",header=None)
    data = pd.read_csv("../DataSample/WADI-10000-GroundTruth.csv", header=None)
    divide = 0.15*4
    num_data = len(data)
    for id in range(10):
        for i in range(int(num_data * divide)):
            bios = int(num_data * random.random())
            if random.random() < 0.5:
                data.iloc[bios, id] = max_lst[id] + max_lst[id] * (0.15 + random.random())
            else:
                data.iloc[bios, id] = min_lst[id] - min_lst[id] * (0.15 + random.random())
    # data.to_csv("../DataSample/PUMP-10000-15%.csv", index=None, header=None)
    data.to_csv("../DataSample/WADI-10000-15%.csv", index=None, header=None)
#
# for i in range(5):
#     print(min_lst[i],",",max_lst[i])
