#!/usr/local/bin/python3.7
# ** coding = utf8 *

from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def machine_test():
   path = "/data/code_trunk/heen/data/sample.csv"
   data = pd.read_csv(path)
   print(data.head(3))
   X = data['AGE']
   Y = data['SCORE']
   X = np.asarray(X).reshape(-1,1)
   Y = np.asarray(Y).reshape(-1,1)
   print(X)
   print(Y)
