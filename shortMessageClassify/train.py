# coding=utf-8

import string,csv,codecs
from tgrocery import Grocery

csvin=codecs.open('train.txt','r','utf-8');
csvout=codecs.open('train1.txt','w','utf-8');
#reader=csv.reader(csvin)
#writer=csv.writer(csvout)
reader=csvin.readlines()

i=0
str=''
trainlist=[]
for line in reader:
    if(i<=1000):
        str=line.split(u'\t')
        csvout.write(str[1]+u','+str[2])
        trainstr=(str[1],str[2])
        trainlist.append(trainstr)
        print str[1]+u','+str[2]
    else:
        if(i==1001):
            grocery=Grocery('sample')
            grocery.train(trainlist)

            rightCount=0
            errorCount=0

        str=line.split(u'\t')
        print line
        result=grocery.predict(str[2])
        print result

        #import pdb; pdb.set_trace()
        if(result==str[1]):
            print 'predict right'
            rightCount=rightCount+1
        else:
            print 'predict error'
            errorCount=errorCount+1

    if(i>2000):
        break

    i=i+1

print rightCount
print errorCount

csvin.close()
csvout.close()

