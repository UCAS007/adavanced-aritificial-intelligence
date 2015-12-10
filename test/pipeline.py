from __future__ import print_function
import json
import pickle
from pprint import pprint
from time import time
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
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

trainNum=200000;
parameters = {
    'vect__max_df': (0.5, 0.75, 1.0),
    #'vect__max_features': (None, 5000, 10000, 50000),
    'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    #'tfidf__use_idf': (True, False),
    'tfidf__norm': ('l1', 'l2'),
    'clf__alpha': (0.00001, 0.000001),
    'clf__penalty': ('l2', 'elasticnet'),
    #'clf__n_iter': (10, 50, 80),
}

if __name__ == "__main__":
    # multiprocessing requires the fork to happen in a __main__ protected
    # block

    # find the best parameters for both the feature extraction and the
    # classifier
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)

    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    pprint(parameters)
    t0 = time()
    grid_search.fit(data[0:trainNum],target[0:trainNum])
    print("done in %0.3fs" % (time() - t0))
    print()

    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
