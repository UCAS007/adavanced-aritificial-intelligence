from __future__ import print_function

import pickle
from pprint import pprint
from time import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
import os
import mydataset

trainFileName='pipelineTrain.pkl'
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

pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(class_weight='balanced')),
])

Y=[]
for i in trainClass:
    if(i==u'0'):
        Y.append(0)
    else:
        Y.append(1)

parameters = {
    ###'vect__max_df': (0.2,0.3,0.4,0.5, 0.55,0.57,0.59,0.61,0.6,0.62,0.63,0.65,0.7,0.75, 1.0),
    'vect__max_df': (0.6,),
    #'vect__max_features': (None, 5000, 10000, 50000),
    ###'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    'vect__ngram_range': ((1, 2),),
    #'tfidf__use_idf': (True, False),
    'tfidf__use_idf': (True,),
    'tfidf__norm': ('l1','l2',),
    #'tfidf__norm': ('l1', 'l2'),
    ###'clf__alpha': (0.00001, 0.000001,1e-08,1e-09,1e-10,1e-11),
    'clf__alpha': (1e-05,1e-07,1e-09,) ,
    #'clf__penalty': ('l2', 'elasticnet'),
    'clf__penalty': ('l2','l1','none','elasticnet'),
    ###'clf__n_iter': (10, 50, 80),
    #'clf__n_iter': (10, 50, 80),
}

if __name__ == "__main__":
    # multiprocessing requires the fork to happen in a __main__ protected
    # block

    # find the best parameters for both the feature extraction and the
    # classifier
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1,scoring='f1',pre_dispatch=2,error_score=0)

    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    pprint(parameters)
    t0 = time()
    #grid_search.fit(data[0:trainNum],target[0:trainNum])
    #trainNum=200000
    #grid_search.fit(trainData[0:trainNum],trainClass[0:trainNum])
    grid_search.fit(trainData,Y)
    print("done in %0.3fs" % (time() - t0))
    print()

    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))