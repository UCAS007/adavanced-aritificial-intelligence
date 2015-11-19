# -*- coding: utf-8 -*-
import codecs

def checkline(line):
    strset=line.split('\t')
    try:
        index=int(strset[0])
    except:
        return False
    else:
        return True

def getcontent(lines,i):
    flag=checkline(lines[i])
    if(flag):
        flag=False
        content=lines[i]
        id=i+1
        N=lines.__len__()
        while((not flag) and id<N):
            flag=checkline(lines[id])
            if(not flag):
                content=content+lines[id]
                id=id+1
                print "preprocessing: "+content+'.'*30
        return content
    else:
        return ''

def splitfile(rawfile,trainfile,validatefile):
    filein=codecs.open(rawfile,'r','utf-8')
    in_reader=filein.readlines()
    N=in_reader.__len__()
    train_num=N*4/5

    train=codecs.open(trainfile,'w','utf-8')
    validate=codecs.open(validatefile,'w','utf-8')
    train.writelines(in_reader[0:train_num])
    validate.writelines(in_reader[train_num+1:])
    train.close()
    validate.close()
    filein.close()

#rawFileName='../data/rawtrain.txt'
#trainFileName='../data/train.txt'
#validateFileName='../data/validate.txt'

#splitfile(rawFileName,trainFileName,validateFileName)

if __name__ == "__main__":
    rawFileName='../data/rawtrain.txt'
    trainFileName='../data/train.txt'
    validateFileName='../data/validate.txt'
    print 'preprocessing: split '+rawFileName+' to '+trainFileName+' and '+validateFileName+'\n'
    splitfile(rawFileName,trainFileName,validateFileName)