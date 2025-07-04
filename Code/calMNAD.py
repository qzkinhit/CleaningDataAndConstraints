import pandas as pd
from bNDCRepair import Detect, Constraint

def SubDataSet(dataSet1, dataSet2):
    n = len(dataSet2)
    sub = 0
    for i in range(n):
        for j in range(2):
            sub += abs(dataSet2.iloc[i,j] - dataSet1.iloc[i,j])
    return sub

def CalMNAD(C,dataSet,dataSet_truth):
    R_our = Detect(C, dataSet)
    MNAD = 0
    r_n = 0
    for c in R_our:
        # print(c[2].feature1,c[2].feature2)
        if c[2].type == 1:
            if dataSet[c[1]].iloc[c[0]]>c[2].feature2:
                repair = c[2].feature2
            else:
                repair = c[2].feature1
        else:
            repair = dataSet[c[1]].iloc[c[0]-1]

        MNAD += abs(dataSet_truth[c[1]].iloc[c[0]]-repair)
        r_n += abs(dataSet[c[1]].iloc[c[0]]-repair)
    return 1-MNAD/(SubDataSet(dataSet_truth,dataSet)+r_n)