# __author__ = 'zhengcs.liu
import math

SPLITSTR = '<>'

def load_data(fileName):
    inputFile = open(fileName)
    dataList = []
    for line in inputFile.readlines():
        adgroupObj = cvtToMap(line)
        dataList.append(adgroupObj)
    inputFile.close()

    return dataList

def cvtToMap(adgroup_line):
    if len(adgroup_line) < 4:
        return {}
    adgroup_arr = adgroup_line.split('\t')
    adgroup_obj = {}
    adgroup_obj['id'] = adgroup_arr[0]
    adgroup_obj['adgroup_id'] = adgroup_arr[1]
    adgroup_obj['thedate'] = adgroup_arr[2]
    adgroup_obj['type'] = adgroup_arr[3]
    adgroup_obj['pv'] = adgroup_arr[4]
    adgroup_obj['gmt_create'] = adgroup_arr[5]
    adgroup_obj['product_id'] = adgroup_arr[6]

    return adgroup_obj

def cvtToK4(adgroupList):
    k4 = {}
    for ad in adgroupList:
        theKey = ad['adgroup_id'] + SPLITSTR + ad['thedate'] + SPLITSTR + ad['type'] + SPLITSTR + ad['pv']
        if theKey in k4:
            k4[theKey] += 1
        else:
            k4[theKey] = 1

    return k4

def cvtToK3(adgroupList):
    k3 = {}
    for ad in adgroupList:
        theKey = ad['adgroup_id'] + SPLITSTR + ad['thedate'] + SPLITSTR + ad['type']
        if theKey in k3:
            k3[theKey] += 1
        else:
            k3[theKey] = 1

    return k3

def findSingleInK4(k4, adgroupList):
    checkResult = []
    for ad in adgroupList:
        k = ad['adgroup_id'] + SPLITSTR + ad['thedate'] + SPLITSTR + ad['type'] + SPLITSTR + ad['pv']
        if k4[k] < 2:
            checkResult.append(ad)
    return checkResult

def findDoubleInK4(k4, adgroupList):
    checkResult = []
    for ad in adgroupList:
        k = ad['adgroup_id'] + SPLITSTR + ad['thedate'] + SPLITSTR + ad['type'] + SPLITSTR + ad['pv']
        if k4[k] > 1:
            checkResult.append(ad)
            k4[k] -= 1
    return checkResult

if __name__ == '__main__':
    print 'i love siyu'
    fileName = 'data/adlimit.data'
    adgroupList = load_data(fileName)
    print 'the num of line is ' + str(len(adgroupList))
    k4 = cvtToK4(adgroupList)
    print 'the num of k4 is ' + str(len(k4))
    k3 = cvtToK3(adgroupList)
    print 'the num of k3 is ' + str(len(k3))

    singleInK4 = findSingleInK4(k4, adgroupList)
    print 'the num of single pv is ' + str(len(singleInK4))
    doubleInK4 = findDoubleInK4(k4, adgroupList)
    print 'the num of double pv is ' + str(len(doubleInK4))
    ids = ''
    for ad in doubleInK4:
        ids += ad['id'] + ','
    print ids

