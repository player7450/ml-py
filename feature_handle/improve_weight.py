import sys
import string
__author__ = 'liuzheng'

def multiple(file_name, times):
    input_file = open(file_name)
    output_file = open(file_name + '_' + str(times), 'w')
    while (True):
        line = input_file.readline().rstrip()
        if len(line) < 4:
            break
        if line.startswith('1'):
            for i in range(0, times, 1):
                output_file.write(line + '\n')
        else:
            output_file.write(line + '\n')
    input_file.close()
    output_file.close()

if __name__=='__main__':
    print 'hehe'
    if len(sys.argv) < 3:
        print 'input file path and multiple factor!'
        exit()
    multiple(sys.argv[1], string.atoi(sys.argv[2]))
