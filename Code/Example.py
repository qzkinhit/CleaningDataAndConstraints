import pandas as pd
from bNDCRepair import Constraint, ConstraintRepair, Detect
from calMNAD import CalMNAD
import time
import os


def IDF_10000_5():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-10000-5%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_10000_10():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-10000-10%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_10000_15():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-10000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_10000_20():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-10000-20%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_10000_25():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-10000-25%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_3000_15():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-3000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-3000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_5000_15():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-5000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-5000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_7000_15():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-7000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-7000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth

def IDF_11000_15():
    ValidSet = pd.read_csv("../DataSample/IDF-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/IDF-11000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/IDF-11000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0, 4000, {0}, 1)
    c2b = Constraint('b', -6, -1, {1}, 1)
    c3b = Constraint('c', 3, 4, {2}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('a', 0, 6475.96387, {0}, 1)
    c2 = Constraint('b', -4.92642, -1.79391, {1}, 1)
    c3 = Constraint('c', 3.2, 3.67739, {2}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth


def SIM_10000_15():
    ValidSet = pd.read_csv("../DataSample/SIM-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/SIM-10000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/SIM-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 11, 13, {0}, 1)
    c2b = Constraint('b', 52, 53, {1}, 1)
    c3b = Constraint('c', 21, 27.5, {2}, 1)
    c4b = Constraint('d', 55, 74, {4}, 1)
    c5b = Constraint('e', -1, 4, {0}, 2)
    c6b = Constraint('f', 1, 2.1, {1, 2}, 3)
    c7b = Constraint('g', 2, 2.1, {0, 3, 4}, 3)
    C = {c2b, c3b, c4b, c6b}

    c1 = Constraint('a', 10, 15, {0}, 1)
    c2 = Constraint('b', 50, 55, {1}, 1)
    c3 = Constraint('c', 25, 27.5, {2}, 1)
    c4 = Constraint('d', 60, 74, {4}, 1)
    c5 = Constraint('e', -1, 1, {0}, 2)
    c6 = Constraint('f', 1.9, 2.1, {1, 2}, 3)
    c7 = Constraint('g', 1.9, 2.1, {0, 3, 4}, 3)
    C_truth = {c2,c3,c4,c6}

    return ValidSet, dataSet, Groundtruth, C, C_truth


def NASDAQ_10000_15():
    ValidSet = pd.read_csv("../DataSample/NASDAQ-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/NASDAQ-10000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/NASDAQ-10000-GroundTruth.csv",header = None)

    c1b = Constraint('c', 0, 0, {0}, 2)
    c2b = Constraint('a', 0, 12000, {0}, 1)
    c3b = Constraint('b', 0, 5000, {1}, 1)
    C = {c1b,c2b,c3b}
    c1 = Constraint('c', 0, 0, {0}, 2)
    c2 = Constraint('a', 252.199997, 10740.475959802348, {0}, 1)
    c3 = Constraint('b', 252.199997, 4000, {1}, 1)
    C_truth = {c1,c2,c3}

    return ValidSet, dataSet, Groundtruth, C, C_truth


def PUMP_10000_15():
    ValidSet = pd.read_csv("../DataSample/PUMP-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/PUMP-10000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/PUMP-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 45, 55, {0}, 1)
    c2b = Constraint('b', 50, 55, {1}, 1)
    c3b = Constraint('c', 40, 55, {2}, 1)
    c4b = Constraint('d', 40, 70, {3}, 1)
    c5b = Constraint('e', 30, 55, {4}, 1)
    c6b = Constraint('f', 80, 135, {5}, 1)
    C = {c1b,c2b,c3b, c4b, c5b, c6b}
    # c1 = Constraint('a', 49.34, 50.61, {0}, 1)
    # c2 = Constraint('b', 51.95, 53.13, {1}, 1)
    # c3 = Constraint('c', 44.31, 47.35, {2}, 1)
    # c4 = Constraint('d', 43.44, 79.43, {3}, 1)
    # c5 = Constraint('e', 35.15, 51.11, {4}, 1)
    # c6 = Constraint('f', 84.89, 132, {5}, 1)
    c1 = Constraint('a', 44.12, 49.28, {0}, 1)
    c2 = Constraint('b', 49.60, 52.13, {1}, 1)
    c3 = Constraint('c', 44.31, 55.25, {2}, 1)
    c4 = Constraint('d', 46.87, 53.64, {3}, 1)
    c5 = Constraint('e', 39.10, 54.95, {4}, 1)
    c6 = Constraint('f', 86.66, 134.98, {5}, 1)
    C_truth = {c1, c2, c3, c4, c5, c6}

    return ValidSet, dataSet, Groundtruth, C, C_truth


def WADI_10000_15():
    ValidSet = pd.read_csv("../DataSample/WADI-ValidSet.csv", header=None)
    dataSet = pd.read_csv("../DataSample/WADI-10000-15%.csv", header=None)
    Groundtruth = pd.read_csv("../DataSample/WADI-10000-GroundTruth.csv",header = None)

    c1b = Constraint('a', 0.6, 0.7, {0}, 1)
    c2b = Constraint('b', 0.3, 0.4, {1}, 1)
    c3b = Constraint('c', 45, 46, {2}, 1)
    c4b = Constraint('d', 2600, 2700, {3}, 1)
    c5b = Constraint('e', 100, 100, {4}, 1)
    c6b = Constraint('f', 0.04, 0.05, {5}, 1)
    c7b = Constraint('g', 0.14, 0.14, {6}, 1)
    c8b = Constraint('h', 100, 100, {7}, 1)
    c9b = Constraint('i', 0.04, 0.05, {8}, 1)
    c10b = Constraint('j', 0.09, 0.09, {9}, 1)
    C = {c1b, c2b, c3b, c4b, c5b, c6b, c7b, c8b, c9b, c10b}
    c1 = Constraint('a', 0.637, 0.8, {0}, 1)
    c2 = Constraint('b', 0.3, 0.35, {1}, 1)
    c3 = Constraint('c', 45, 46, {2}, 1)
    c4 = Constraint('d', 2600, 2700, {3}, 1)
    c5 = Constraint('e', 99.5, 100.5, {4}, 1)
    c6 = Constraint('f', 0.04, 0.05, {5}, 1)
    c7 = Constraint('g', 0.14, 0.15, {6}, 1)
    c8 = Constraint('h', 99.5, 100.5, {7}, 1)
    c9 = Constraint('i', 0.04, 0.05, {8}, 1)
    c10 = Constraint('j', 0.09, 0.09, {9}, 1)
    C_truth = {c1, c2, c3, c4, c5, c6, c7, c8, c9, c10}

    return ValidSet, dataSet, Groundtruth, C, C_truth


if __name__ == '__main__':
    start = time.time()
    
    ValidSet, dataSet, Groundtruth, C, C_truth = IDF_10000_15()
    # ValidSet, dataSet, Groundtruth, C, C_truth = SIM_10000_15()
    # ValidSet, dataSet, Groundtruth, C, C_truth = NASDAQ_10000_15()
    # ValidSet, dataSet, Groundtruth, C, C_truth = PUMP_10000_15()
    # ValidSet, dataSet, Groundtruth, C, C_truth = WADI_10000_15()

    # Call the algorithm
    C_new = ConstraintRepair(dataSet, C, lamb=0.0000004, delta=1, alpha=0, Validation=ValidSet, miu=3, max_T=50,
                             confidence=0.8, omg=0.001)

    # Print results
    for c in C_new:
        print(c.name, end='')
        print("[", end='')
        print(c.feature1, c.feature2, end='')
        print("]")

    # Calculate Precision and Recall
    R_our = Detect(C_new, dataSet)
    R_truth = Detect(C_truth, dataSet)


    Point_our = set()
    Point_truth = set()
    Point_all = set()

    for point in R_our:
        Point_our.add((point[0],point[1]))

    for pp in R_truth:
        Point_truth.add((pp[0],pp[1]))

    for i in range(len(dataSet)):
        for j in range(len(dataSet.columns)):
            Point_all.add((i,j))

    TP = len(Point_all - (Point_our | Point_truth))
    TN = len(Point_our & Point_truth)
    FP = len((Point_all-Point_our)&Point_truth)
    FN = len(Point_our & (Point_all-Point_truth))
    print(TP,TN,FP,FN)

    P = TP/(TP+FP)
    R = TP/(FN+TP)
    print('Precision: '+str(TP/(TP+FP)), 'Recall: '+str(TP/(FN+TP)))
    print('MNAD: '+str(CalMNAD(C_new, dataSet, Groundtruth)))

    end = time.time()
    print('Runtime', end - start, 's')