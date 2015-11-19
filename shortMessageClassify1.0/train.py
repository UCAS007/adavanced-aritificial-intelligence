# coding=utf-8

import csv,codecs
from tgrocery import Grocery
import preprocessing as pp

rawFileName='../data/rawtrain.txt'
trainFileName='../data/train.txt'
validateFileName='../data/validate.txt'

#pp.splitfile(rawFileName,trainFileName,validateFileName)

str=''
trainlist=[]
# train #################################
filein=codecs.open(trainFileName,'r','utf-8')
in_reader=filein.readlines()
i=0
for line in in_reader:
    content=pp.getcontent(in_reader,i)
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
        trainstr=(str[1],content[len+4:])
        trainlist.append(trainstr)

print 'train start '+'.'*30
#grocery=Grocery('sample')
grocery=Grocery('version1.0')
grocery.train(trainlist)
grocery.save()
filein.close()
print 'train end '+'.'*30


