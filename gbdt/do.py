from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

def test(a = 1, b = 2):
    print str(a)
    print str(b)

def logistic_regression():
    print '.. logistic regression ..'
    X, y = make_hastie_10_2(random_state=0)
    X_train, X_test = X[:2000], X[2000:]
    y_train, y_test = y[:2000], y[2000:]
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    lr_predict_labels = lr.predict(X_test)
    print sum(lr_predict_labels==y_test)

def gbdt():
    print '.. gbdt ..'
    X, y = make_hastie_10_2(random_state=0)
    X_train, X_test = X[:2000], X[2000:]
    y_train, y_test = y[:2000], y[2000:]
    gbdt = GradientBoostingClassifier(n_estimators=10, learning_rate=1.0,\
                                     max_depth=3, random_state=0).fit(X_train, y_train)
    # clf.fit(X_train, y_train)
    gbdt.fit(X_train, y_train)
    print gbdt.feature_importances_
    print gbdt.feature_importances_.shape
    gbdt_predict_label = gbdt.predict(X_test)
    print len(y_test)
    print y_test
    print sum(gbdt_predict_label==y_test)

def foo():
    result = []
    index = 0
    count = 0
    file = open("modelInfo.txt")
    fea_map = {}
    for line in file.readlines():
        if len(line) < 4:
            break
        if line.startswith("booster"):
            index += 1
            count = 0
            if 1 != index:
                result.append(fea_map)
                fea_map = {}
        elif line.__contains__("leaf"):
            count += 1
            fea_map[line[line.rindex('\t') + 1 : line.index(':')]] = count
            # fea_map[count] = line
    result.append(fea_map)
    file.close()
    print 'number of tree = ' + str(len(result))
    max_num_leaf = 0
    for f in result:
        if len(f) > max_num_leaf:
            max_num_leaf = len(f)
    print 'max num of leaves = ' + str(max_num_leaf)

if __name__=='__main__':
    print 'hehe'
    # gbdt()
    logistic_regression()
