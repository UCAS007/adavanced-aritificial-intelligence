"""
Fmax=0.994336 name=Perceptron
Fmax=0.975841 name=SGD
i=1 name=Passive-Aggressive I F=0.956934 use time=340.085862 s
i=2 name=Passive-Aggressive II F=0.982147 use time=378.754161 s
i=3 name=SAG F=0.622018 use time=387.336895 s
name=nuSVC ValueError: specified nu is infeasible
"""
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier,Perceptron,PassiveAggressiveClassifier,LogisticRegression
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn import metrics
import jieba
import mydataset
import os
import csv,codecs
import preprocessing as pp
import time
from sklearn.svm import NuSVC

def train(clf=SGDClassifier(class_weight='balanced')):
    trainFileName='train.pkl'
    testFileName='test.pkl'
    pipelineFileName='pipeline.pkl'

    if(os.path.exists(trainFileName)):
        fin=open(trainFileName,'r')
        trainData=pickle.load(fin)
        trainClass=pickle.load(fin)
        fin.close()
    else:
        trainText=mydataset.getAllTrainTextList()
        i=0;
        N=trainText.__len__()
        trainData=[]
        trainClass=[]
        for (tag,text) in trainText:
            i=i+1
            if(i%5000==0):
                print('i=%08d finished %5.5f%% using jieba to cut the text\n'%(i,i*100.0/N))

            trainData.append(text)
            trainClass.append(tag)

        fout=open(trainFileName,'w')
        pickle.dump(trainData,fout)
        pickle.dump(trainClass,fout)
        fout.close()

    #if(os.path.exists(pipelineFileName)):
    if(False):
        fin=open(pipelineFileName,'r')
        pipeline=pickle.load(fin)
        fin.close()
    else:
        pipeline = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', clf),
        ])

        pipeline.set_params(vect__max_df=0.6,tfidf__norm='l1',tfidf__use_idf=True,vect__ngram_range=(1,2))
        trainNum=trainData.__len__()
        pipeline.fit(trainData[0:trainNum],trainClass[0:trainNum])

        fout=open(pipelineFileName,'w')
        pickle.dump(pipeline,fout)
        fout.close()


    #################################### output train result
    trainNum=trainData.__len__()
    #print 'train result '+"#"*30
    prec=pipeline.predict(trainData[0:trainNum])
    expected=trainClass[0:trainNum]

    #print("Classification report for classifier:\n%s\n"
          #% (metrics.classification_report(expected, prec)))

    TP=0.0
    TN=0.0
    FP=0.0
    FN=0.0

    N=trainData.__len__()
    for i in range(0,trainNum):
        if(prec[i]==expected[i]):
            if(prec[i]==u'1'):
                TP=TP+1
            else:
                TN=TN+1
        else:
            if(prec[i]==u'1'):
                FP=FP+1
            else:
                FN=FN+1

    P=TP/(TP+FP)
    R=TP/(TP+FN)
    F=2*P*R/(P+R)

    #print('train result: P=%f,R=%f,F=%f\n'%(P,R,F))

    return F,pipeline

############################################# output test result

if __name__ == '__main__' :
    trainFileName='train.pkl'
    testFileName='test.pkl'
    pipelineFileName='pipeline.pkl'
    bestPipelineFileName='bestAlgorithm.pkl'

    Fmax=0
    classifiers = [
        #("SGD", SGDClassifier(clf__alpha=1e-07,clf__penalty='l2')),
        #("ASGD", SGDClassifier(clf__alpha=1e-07,clf__penalty='l2',average=True)),
        #("BSGD", SGDClassifier(clf__alpha=1e-07,clf__penalty='l2',class_weight='balanced')),
        #("Perceptron", Perceptron()),
        #("Passive-Aggressive I", PassiveAggressiveClassifier(loss='hinge',
                                                         #C=1.0)),
        #("Passive-Aggressive II", PassiveAggressiveClassifier(loss='squared_hinge',
                                                              #C=1.0)),
        #("SAG", LogisticRegression(solver='sag', tol=1e-1)),
        #("NuSVC",NuSVC())
    ]

    i=0
    FScores=[]
    for name,clf in classifiers:

        i=i+1
        t1=time.time()
        F,pipeline=train(clf)
        t2=time.time()

        FScores.append(F)

        if(F>Fmax):
            Fmax=F
            bestPipeline=pipeline
            print('Fmax=%f name=%s \n'%(Fmax,name))

        print ('i=%d name=%s F=%f use time=%f s\n'%(i,name,F,t2-t1))
    fout=open(bestPipelineFileName,'w')
    pickle.dump(bestPipeline,fout)
    fout.close()
    print('Fmax=%f \n' % (Fmax))

    if(os.path.exists(testFileName)):
        fin=open(testFileName,'r')
        testText=pickle.load(fin)
        fin.close()
    else:
        testText=mydataset.getTestTextList()
        fout=open(testFileName,'w')
        pickle.dump(testText,fout)
        fout.close()

    outputFileName='../output/upload.csv'
    fileOutput=codecs.open(outputFileName,'w','utf-8')

    prec=pipeline.predict(testText)
    N=800001
    for i in prec:
        fileOutput.write(N.__str__()+','+i+'\n')
        N=N+1

    fileOutput.close()