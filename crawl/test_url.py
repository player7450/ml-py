import urllib2

__author__ = 'liuzheng'

def test_url():
    r = urllib2.urlopen("http://www.baidu.com");
    url_text = r.read()
    print url_text

def foo():
    a = [1,2,3,4]
    print a
    a.append(5)
    print a
    b = tuple(a)
    print b
    c = (1,2,3,4)

if __name__=='__main__':
    print 'hehe'
    # test_url()
    foo()
