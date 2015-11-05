# coding=utf-8

import csv,codecs
from tgrocery import Grocery

trainFileName='train.txt'
testFileName='test.txt'
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
        continue

    #print count
    #print str
    trainstr=(str[1],str[2])
    trainlist.append(trainstr)
    #print str[1]+u','+str[2]

print 'start train'
grocery=Grocery('sample')
grocery.train(trainlist)
grocery.save()
filein.close()


# test ##################################
print 'start test'
filetest=codecs.open(testFileName,'r','utf-8')
test_reader=filetest.readlines()

resultlist=[]
for line in test_reader:
    str=line.split(u'\t')
    count=str.__len__()
    if(count<2):
        continue

    result=grocery.predict(str[1])
    resultlist.append((str[0],result))

filetest.close()

# write result to result.txt #######################
print 'start write'
fileout=codecs.open(outputFileName,'w','utf-8')
csvout=csv.writer(fileout)
csvout.writerows(resultlist)
fileout.close()