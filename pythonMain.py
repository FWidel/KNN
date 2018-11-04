import pandas as pd
import numpy as np
import knnAlgorithm as knn

learningDataArray = np.array(pd.read_csv("iris.datalearning.csv"))
testDataArray = np.array(pd.read_csv("iris.datatest.csv"))
kn = knn.knnAlgorithm(3, learningDataArray)
print(kn.score(testDataArray, kn.predict(testDataArray)))