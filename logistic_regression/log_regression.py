# __author__ = 'liuzheng'
from numpy import *
import matplotlib.pyplot as plt
import time

def sigmoid(a):
    return 1.0 / (1 + exp(-a))

def train_log_regres(train_x, train_y, opts):
    start_time = time.time()
    num_samples, num_features = shape(train_x)
    alpha = opts['alpha']; max_iter = opts['max_iter']
    weights = ones((num_features, 1))

    for k in range(max_iter):
        if opts['optimize_type'] == 'grad_descent':
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
        elif opts['optimize_type'] == 'smooth_grad_descent':
            data_index = range(num_samples)
            for i in range(num_samples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                rand_index = int(random.uniform(0, len(data_index)))
                output = sigmoid(train_x[rand_index, :] * weights)
                error = train_y[rand_index, 0] - output
                weights = weights + alpha * train_x[rand_index, :].transpose() * error
                del(data_index[rand_index])
        else:
            raise NameError('not support optimize method type!')

    print 'training complete! took %fs!' % (time.time() - start_time)
    return weights

def test_log_regres(weights, test_x, test_y):
    num_samples, num_features = shape(test_x)
    match_count = 0
    for i in xrange(num_samples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        if predict == bool(test_y[i, 0]):
            match_count += 1
        accuracy = float(match_count) / num_samples
        return accuracy

def show_log_regres(weights, train_x, train_y):
    num_samples, num_features = shape(train_x)
    if num_features != 3:
        print "sorry! cannot draw because the dimension is not 2"
        return 1
    for i in xrange(num_samples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')

    min_x = min(train_x[:,1])[0, 0]
    max_x = max(train_x[:,1])[0, 0]
    weights = weights.getA()
    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()


