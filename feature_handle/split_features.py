import sys
import string

def split_file(file_path):
    file = open(file_path)
    output1 = open(file_path + '_1', 'w')
    output2 = open(file_path + '_2', 'w')
    try:
        while (True):
            line_text = file.readline()
            if len(line_text) < 4:
                break
            features = line_text[line_text.index('\t') + 1:].rstrip().split(' ')
            new_feas = ['','']
            for fea in features:
                if (string.atoi(fea.split(':')[0]) < 3100):
                    new_feas[0] += fea + ' '
                else:
                    new_feas[1] += fea + ' '
            flag = line_text[0]
            if len(new_feas[0]) > 0:
                output1.write(flag + '\t' + new_feas[0] + '\n')
            if len(new_feas[1]) > 0:
                output2.write(flag + '\t' + new_feas[1] + '\n')
    except Exception,e:
        print e
    finally:
        file.close()
        output1.close()
        output2.close()

def test():
    ss = 'he\the'
    print ss + ('haha')
    print ss.index('\t')

if __name__=='__main__':
    print 'hehe'
    # test()
    split_file(sys.argv[1])
