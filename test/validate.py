# -*- coding: utf-8 -*-
import csv,codecs
from tgrocery import Grocery
import preprocessing as pp

trainFileName='../data/train.txt'
validateFileName='../data/validate.txt'
outputFileName='../output/result.txt'

# validate ##################################
#grocery=Grocery('sample')
grocery=Grocery('version1.0')
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
    content=pp.getcontent(validate_reader,i)
    i=i+1
    if(i%5000==0):
        print ("%d "%(i))+'#'*30
    #if(i>10):
        #break
    if(content==''):
        print line
    else:
        str=content.split('\t')
        len=str[0].__len__()
        result=grocery.predict(content[len+3:])
        if(result==str[1]):
            if(str[1]==u'0'):
                TN=TN+1
            else:
                TP=TP+1
        else:
            if(str[1]==u'0'):
                FP=FP+1
                fileOutput.write('FP: '+line+' \n')
            else:
                FN=FN+1
                fileOutput.write('FN: '+line+' \n')

precision=TP/(TP+FP)
recall=TP/(TP+FN)

P1=precision
R1=recall
F1=0.65*P1+0.35*R1
P0=TN/(TN+FN)
R0=TN/(TN+FP)
F0=0.65*P0+0.35*R0

F=0.7*F1+0.3*F0

print 'result is : '+"."*30
print precision
print recall
print F1
print F0
print F

fileValidate.close()
fileOutput.close()