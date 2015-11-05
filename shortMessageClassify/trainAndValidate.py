# coding=utf-8

import csv,codecs
from tgrocery import Grocery

trainFileName='post_train.txt'
validateFileName='post_validate.txt'
outputFileName='result.txt'

str=''
trainlist=[]
# train #################################
filein=codecs.open(trainFileName,'r','utf-8')
in_reader=filein.readlines()
i=0
for line in in_reader:
    i=i+1
    if(i%5000==0):
        print ("%d "%(i))+'#'*30
    str=line.split(u',')
    count=str.__len__()
    if(count<2):
        print 'error happen'+"#"*30
        continue

    #print count
    #print str
    trainstr=(str[0],str[1])
    trainlist.append(trainstr)
    #print str[1]+u','+str[2]

grocery=Grocery('sample')
grocery.train(trainlist)
grocery.save()
filein.close()


# test ##################################
print 'start test'
TP=0.0
TN=0.0
FP=0.0
FN=0.0

filetest=codecs.open(validateFileName,'r','utf-8')
test_reader=filetest.readlines()

resultlist=[]
for line in test_reader:
    str=line.split(u',')
    #import pdb; pdb.set_trace()
    #print line
    result=grocery.predict(str[1])
    #print result
    #import pdb; pdb.set_trace()
    if(result==str[0]):
        if(str[0]==u'0'):
            TN=TN+1
        else:
            TP=TP+1
    else:
        if(str[0]==u'0'):
            FP=FP+1
        else:
            FN=FN+1

precision=TP/(TP+FP)
recall=TP/(TP+FN)
F=2*precision*recall/(precision+recall)

print 'result is : '+"."*30
print precision
print recall
print F

filetest.close()