import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn import metrics
import jieba
import train
import os


if(os.path.exists('jointext.json')):
    fin=open('jointext.json','r')
    jointext=json.load(fin)
    fin.close()
else:
    jointext=train.getTrainTextList()
    fout=open('jointext.json','w')
    json.dump(jointext,fout)
    fout.close()

if(os.path.exists('text_cut.pickle')):
    fin=open('text_cut.pickle','r')
    data=pickle.load(fin)
    target=pickle.load(fin)
    fin.close()
else:
    data=[]
    target=[]
    i=0;
    N=jointext.__len__()
    for (tag,text) in jointext:
        i=i+1
        if(i%5000==0):
            print('i=%08d finished %5.5f%% using jieba to cut the text\n'%(i,i*100.0/N))
        seg_list=jieba.cut(text,cut_all=False)
        text_cut=" ".join(seg_list)
        data.append(text_cut)
        target.append(tag)

    fout=open('text_cut.pickle','w')
    pickle.dump(data,fout)
    pickle.dump(target,fout)
    fout.close()

#cv=CountVectorizer()
#tfidf=TfidfTransformer()
#data_cv=cv.transform(data)
#data_tfidf=tfidf.transform(data_cv)
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(class_weight='balanced')),
])


pipeline.set_params(vect__max_df=1.0,clf__alpha=0.00001,clf__penalty='l2',vect__ngram_range=(1,1))
trainNum=data.__len__()
pipeline.fit(data[0:trainNum],target[0:trainNum])

fout=open('pipeline.pkl','w')
pickle.dump(pipeline,fout)
fout.close()


#################################################
print 'train result '+"#"*30
prec=pipeline.predict(data[0:trainNum])
expected=target[0:trainNum]

print("Classification report for classifier:\n%s\n"
      % (metrics.classification_report(expected, prec)))

TP=0.0
TN=0.0
FP=0.0
FN=0.0

N=data.__len__()
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