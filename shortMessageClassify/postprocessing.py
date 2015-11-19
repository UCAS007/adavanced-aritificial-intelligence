# coding=utf-8

import codecs

raw_filename='train.txt'
train_filename='post_train.txt'
validate_filename='post_validate.txt'

raw_file=codecs.open(raw_filename,'r','utf-8')
train_file=codecs.open(train_filename,'w','utf-8')
validate_file=codecs.open(validate_filename,'w','utf-8')

train_data=raw_file.readlines()
train_set=[]
train_str=('','')
i=0
for line in train_data:
    split_str=line.split('\t')
    #print split_str
    i=i+1
    if(i%5000==0):
        print ("%d "%(i))+"#"*10
    count=split_str.__len__()
    if(count<3):
        print "."*100
        print ("%d count<3 \n line=%s trainstr=%s"
            % (i,line,train_str))
        train_set.pop()
        #import pdb; pdb.set_trace()
        train_str=train_str+split_str[0]
        print train_str
        train_set.append(train_str)

        #import pdb; pdb.set_trace()
        continue

    train_str=split_str[1]+','+split_str[2]
    train_set.append(train_str)

raw_len=train_set.__len__()
train_num=raw_len*4/5
train_file.writelines(train_set[0:train_num])
validate_file.writelines(train_set[train_num:raw_len])
train_file.close()
validate_file.close()
raw_file.close()

print 'log'+'.'*100
print raw_len
print train_num