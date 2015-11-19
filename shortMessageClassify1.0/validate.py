# -*- coding: utf-8 -*-
import csv,codecs
from tgrocery import Grocery

trainFileName='../data/train.txt'
validateFileName='../data/validate.txt'
outputFileName='../output/result.txt'

# validate ##################################
grocery=Grocery('sample')
grocery.load()

print 'start test'
TP=0.0
TN=0.0
FP=0.0
FN=0.0

fileValidate=codecs.open(validateFileName,'r','utf-8')
validate_reader=fileValidate.readlines()

fileOutput=codecs.open(outputFileName,'w','utf-8')

resultlist=[]
i=0
for line in validate_reader:
    i=i+1
     if(i%5000==0):
        print ("%d "%(i))+'#'*30

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
            fileOutput.write('FP: '+line+' \n')
        else:
            FN=FN+1
            fileOutput.write('FN: '+line+' \n')

precision=TP/(TP+FP)
recall=TP/(TP+FN)
F=2*precision*recall/(precision+recall)


print 'result is : '+"."*30
print precision
print recall
print F

fileValidate.close()
fileOutput.close()