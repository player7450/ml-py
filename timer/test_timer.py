import time
from threading import Timer

__author__ = 'liuzheng'

def print_time(mtime):
    print 'now is ', time.time(), 'mtime is ', mtime
if __name__=='__main__':
    print time.time()
    Timer(5, print_time, (time.time(),)).start()
    Timer(10, print_time, (time.time(), )).start()
    print time.time()
