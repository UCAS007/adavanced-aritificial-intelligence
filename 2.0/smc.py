import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn import metrics
import jieba
import mydataset
import os
import csv,codecs
import preprocessing as pp

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

if(os.path.exists(pipelineFileName)):
    fin=open(pipelineFileName,'r')
    pipeline=pickle.load(fin)
    fin.close()
else:
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(class_weight='balanced')),
    ])

	#clf__alpha: 1e-07
	#clf__penalty: 'l2'
	#tfidf__norm: 'l1'
	#tfidf__use_idf: True
	#vect__max_df: 0.6
	#vect__ngram_range: (1, 2)

    pipeline.set_params(vect__max_df=0.6,clf__alpha=1e-07,clf__penalty='l2',tfidf__norm='l1',tfidf__use_idf=True,vect__ngram_range=(1,2))
    trainNum=trainData.__len__()
    pipeline.fit(trainData[0:trainNum],trainClass[0:trainNum])

    fout=open(pipelineFileName,'w')
    pickle.dump(pipeline,fout)
    fout.close()


#################################### output train result
trainNum=trainData.__len__()
print 'train result '+"#"*30
prec=pipeline.predict(trainData[0:trainNum])
expected=trainClass[0:trainNum]

print("Classification report for classifier:\n%s\n"
      % (metrics.classification_report(expected, prec)))

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

print('train result: P=%f,R=%f,F=%f\n'%(P,R,F))

############################################# output test result

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