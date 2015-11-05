# coding=utf-8

import csv,codecs
from tgrocery import Grocery

trainFileName='xaa'
testFileName='xab'
outputFileName='result.txt'

str=''
trainlist=[]
# train #################################
filein=codecs.open(trainFileName,'r','utf-8')
in_reader=filein.readlines()
for line in in_reader:
    str=line.split(u'\t')
    count=str.__len__()
    if(count<3):
        break

    #print count
    #print str
    trainstr=(str[1],str[2])
    trainlist.append(trainstr)
    #print str[1]+u','+str[2]

grocery=Grocery('sample')
grocery.train(trainlist)
filein.close()


# test ##################################
print 'start test'
TP=0.0
TN=0.0
FP=0.0
FN=0.0

filetest=codecs.open(testFileName,'r','utf-8')
test_reader=filetest.readlines()

resultlist=[]
for line in test_reader:
    str=line.split(u'\t')
    #import pdb; pdb.set_trace()
    #print line
    result=grocery.predict(str[2])
    resultlist.append((str[0],result))
    #print result
    #import pdb; pdb.set_trace()
    if(result==str[1]):
        if(str[1]==u'0'):
            TN=TN+1
        else:
            TP=TP+1
    else:
        if(str[1]==u'0'):
            FP=FP+1
        else:
            FN=FN+1

precision=TP/(TP+FP)
recall=TP/(TP+FN)
F=2*precision*recall/(precision+recall)
print precision
print recall
print F

filetest.close()

# write result to result.txt #######################
fileout=codecs.open('result.txt','w','utf-8')
csvout=csv.writer(fileout)
csvout.writerows(resultlist)
fileout.close()