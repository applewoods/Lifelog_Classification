import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def sklearn_model_score(y_true, y_pred, average= 'macro'):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average= average)
    recall = recall_score(y_true, y_pred, average= average)
    f1 = f1_score(y_true, y_pred, average= average)

    print(f'{average} 평균')
    print('Accuracy : {0:0.6f}'.format(accuracy))
    print('Precision({})'.format(average), ': {0:0.6f}'.format(precision))
    print('Recall({})'.format(average), ': {0:0.6f}'.format(recall))
    print('F1-score({})'.format(average), ': {0:0.6f}\n'.format(f1))

def exist_model_score(y_true, y_pred, average= 'weighted'):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average= average)
    recall = recall_score(y_true, y_pred, average= average)
    f1 = f1_score(y_true, y_pred, average= average)

    accuracy = np.mean(accuracy)
    precision = np.mean(precision)
    recall = np.mean(recall)
    f1 = np.mean(f1)

    print(f'{average} 평균')
    print('Accuracy : {0:0.6f}'.format(accuracy))
    print('Precision({})'.format(average), ': {0:0.6f}'.format(precision))
    print('Recall({})'.format(average), ': {0:0.6f}'.format(recall))
    print('F1-score({})'.format(average), ': {0:0.6f}\n'.format(f1))