# coding=utf-8

import csv,codecs
from tgrocery import Grocery

trainFileName='../data/train.txt'
validateFileName='../data/validate.txt'
outputFileName='../output/result.txt'

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


