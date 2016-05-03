# coding=utf-8

import csv,codecs
from tgrocery import Grocery
import preprocessing as pp
import jieba

def getTrainTextList(cutModel=False):
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
            cuttext=jieba.cut(content[len+3:].strip(),cut_all=cutModel)
            jointext=' '.join(cuttext)
            trainstr=(str[1],jointext)
            trainlist.append(trainstr)

    filein.close()
    return trainlist

def getValidateTextList(cutModel=False):
    rawFileName='../data/rawtrain.txt'
    trainFileName='../data/train.txt'
    validateFileName='../data/validate.txt'

    #pp.splitfile(rawFileName,trainFileName,validateFileName)

    str=''
    trainlist=[]
    # train #################################
    filein=codecs.open(validateFileName,'r','utf-8')
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
            cuttext=jieba.cut(content[len+3:].strip(),cut_all=cutModel)
            jointext=' '.join(cuttext)
            trainstr=(str[1],jointext)
            trainlist.append(trainstr)

    filein.close()
    return trainlist

def getAllTrainTextList(cutModel=False):
    rawFileName='../data/rawtrain.txt'
    trainFileName='../data/train.txt'
    validateFileName='../data/validate.txt'

    #pp.splitfile(rawFileName,trainFileName,validateFileName)

    str=''
    trainlist=[]
    # train #################################
    filein=codecs.open(rawFileName,'r','utf-8')
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
            cuttext=jieba.cut(content[len+3:].strip(),cut_all=cutModel)
            jointext=' '.join(cuttext)
            trainstr=(str[1],jointext)
            trainlist.append(trainstr)

    filein.close()
    return trainlist


def getTestTextList(cutModel=False):
    testFileName='../data/test.txt'

    filetest=codecs.open(testFileName,'r','utf-8')
    test_reader=filetest.readlines()
    testTextList=[]

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
            #result=pipeline.predict(content[len+1:])
            cuttext=jieba.cut(content[len+1:].strip(),cut_all=cutModel)
            jointext=' '.join(cuttext)
            testTextList.append(jointext)

    filetest.close()
    return testTextList

def train():
    print 'train start '+'.'*30
    #grocery=Grocery('sample')
    grocery=Grocery('version1.0')
    grocery.train(trainlist)
    grocery.save()
    print 'train end '+'.'*30

if __name__ == '__main__' :
    train()


