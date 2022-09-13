from ast import Return
import os

import pandas as pd
import numpy as np
import joblib

from tqdm import tqdm

from sklearn.preprocessing import MinMaxScaler

scaler_path = './models/'

def train_test():
    # Train Data
    trainsetList = list(np.load('./Data/TrainData/SelectedTrainSet/trainsetList.npy'))

    life_log = pd.DataFrame(columns=['Date', 'HH', 'MM', 'Heartrate', 'Step', 'Status'])
    for filename in tqdm(trainsetList):
        tmp = pd.read_excel('./Data/TrainData/' + filename)
        life_log = pd.concat([life_log, tmp])

    train_X = life_log[['HH', 'MM', 'Heartrate', 'Step']]
    train_y = life_log[['Status']]
    train_y = train_y.apply(pd.to_numeric, errors= 'coerce')

    # Train Data Normalization
    if os.path.isfile(scaler_path + 'scaler_train_.pkl'):
        minmax_scaler = MinMaxScaler()
        minmax_scaler.fit(train_X)
        train_X = minmax_scaler.transform(train_X)

        joblib.dump(minmax_scaler, scaler_path + 'scaler_train_.pkl')

    else:
        scaler = joblib.load(scaler_path + 'scaler_train_.pkl')
        train_X = scaler.transform(train_X)        

    # Test Data
    testsetList = list(np.load('./Data/TestData/SelectedTestSet/testsetList.npy'))

    life_log_test = pd.DataFrame(columns=['Date', 'HH', 'MM', 'Heartrate', 'Step', 'Status'])
    for filename in tqdm(testsetList):
        tmp = pd.read_excel('./Data/TestData/' + filename)
        life_log_test = pd.concat([life_log_test, tmp])

    test_X = life_log_test[['HH', 'MM', 'Heartrate', 'Step']]
    test_y = life_log_test[['Status']]
    test_y = test_y.apply(pd.to_numeric, errors= 'coerce')

    # Test Data Normalization
    minmax_scaler_test = joblib.load(scaler_path + 'scaler_train_.pkl')
    test_X = minmax_scaler_test.transform(test_X)

    if not os.path.isfile(scaler_path + 'scaler_test_.pkl'):
        joblib.dump(minmax_scaler_test, scaler_path + 'scaler_test_.pkl')

    return train_X, train_y, test_X, test_y