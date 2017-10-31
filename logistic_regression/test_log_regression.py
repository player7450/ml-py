from numpy import *
from log_regression import *
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import time

def load_data():
    train_x = []
    train_y = []
    file_in = open('../data/test_data')
    for line in file_in.readlines():
        line_items = line.strip().split()
        train_x.append([1.0, float(line_items[0]), float(line_items[1])])
        train_y.append(float(line_items[2]))
    return mat(train_x), mat(train_y).transpose()

def test_log():
    # load data
    print '1 --> load data ..'
    train_x, train_y = load_data()
    test_x = train_x; test_y = train_y
    # training ...
    print '2 --> training ..'
    opts = {'alpha' : 0.01, 'max_iter': 200, 'optimize_type': 'grad_descent'}
    optimal_weights = train_log_regres(train_x, train_y, opts)
    print optimal_weights
    # test
    print '3 --> testing ..'
    accuracy = test_log_regres(optimal_weights, test_x, test_y)
    print accuracy
    # show the result
    print '4 --> show result ..'
    print 'the classify accuracy is: %.3f%%' % (accuracy * 100)
    show_log_regres(optimal_weights, train_x, train_y)

def test_log2():
    iris = load_iris()
    samples = iris.data
    # print samples
    target = iris.target

    classifier = LogisticRegression()
    classifier.fit(samples, target)

    x = classifier.predict([5, 3, 5, 2.5])
    print 'hehe --> '
    print x

if __name__ == '__main__':
    test_log2()
