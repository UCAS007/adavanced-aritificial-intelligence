# -*- coding: utf-8 -*-
import csv,codecs
from tgrocery import Grocery
import preprocessing as pp

testFileName='../data/test.txt'
outputFileName='../output/upload.csv'

# test ##################################
#grocery=Grocery('sample')
grocery=Grocery('version1.0')
grocery.load()

print 'start test'

filetest=codecs.open(testFileName,'r','utf-8')
test_reader=filetest.readlines()

fileOutput=codecs.open(outputFileName,'w','utf-8')

i=0
for line in test_reader:
    content=pp.getcontent(test_reader,i)
    i=i+1
    #if(i>10):
        #break
    if(i%5000==0):
        print ("%d "%(i))+'#'*30

    if(content==''):
        print "test.py#"*3+line
    else:
        str=content.split('\t')
        len=str[0].__len__()
        result=grocery.predict(content[len+1:])
        fileOutput.write(str[0]+','+result+'\n')

filetest.close()
fileOutput.close()