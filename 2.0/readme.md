# reference
- http://scikit-learn.org/stable/auto_examples/index.html#working-with-text-documentss
- http://scikit-learn.org/stable/auto_examples/model_selection/grid_search_text_feature_extraction.html#
- http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer
- http://scikit-learn.org/stable/auto_examples/text/document_classification_20newsgroups.html#example-text-document-classification-20newsgroups-pys
- http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/

# CountVectorizer 
- sklearn.feature_extraction.text.CountVectorizer

```
In [52]: y=d.fit_transform(['hello the world','good job 不好 快跑'],None)

In [53]: print y
  (0, 1)	1
  (0, 3)	1
  (0, 4)	1
  (1, 0)	1
  (1, 2)	1
  (1, 5)	1
  (1, 6)	1
```

# fast start text classifys
- http://scikit-learn.org/stable/auto_examples/text/document_clustering.html#example-text-document-clustering-py

# result
```
done in 1213.592s

Best score: 0.997
Best parameters set:
	clf__alpha: 1e-06
	clf__penalty: 'l2'
	vect__max_df: 1.0
	vect__ngram_range: (1, 2)
```

# jieba
```
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
```

---

```
【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学

【精确模式】: 我/ 来到/ 北京/ 清华大学

【新词识别】：他, 来到, 了, 网易, 杭研, 大厦    (此处，“杭研”并没有在词典中，但是也被Viterbi算法识别出来了)

【搜索引擎模式】： 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造
```
---
```
全模式：
done in 976.956s

Best score: 0.958
Best parameters set:
	clf__alpha: 1e-09
	clf__penalty: 'l2'
	vect__max_df: 0.62
	vect__ngram_range: (1, 2)

done in 991.161s

Best score: 0.991
Best parameters set:
	clf__alpha: 1e-09
	clf__penalty: 'l2'
	vect__max_df: 0.5
	vect__ngram_range: (1, 2)

done in 1180.453s

Best score: 0.977
Best parameters set:
	clf__alpha: 1e-07
	clf__penalty: 'l2'
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)

done in 2157.523s

Best score: 0.981
Best parameters set:
	clf__alpha: 1e-07
	clf__penalty: 'l2'
	tfidf__norm: 'l2'
	tfidf__use_idf: True
	vect__max_df: 0.5
	vect__ngram_range: (1, 2)
```
# test/b.py train and validate
```
P=TP/(TP+FP)
R=TP/(TP+FN)
F=2*P*R/(P+R)

pipeline.set_params(vect__max_df=1.0,clf__alpha=0.00001,clf__penalty='l2',vect__ngram_range=(1,2))

train result: P=0.973347,R=0.999111,F=0.986061
validate result: P=0.822481,R=0.980710,F=0.894653

pipeline.set_params(vect__max_df=1.0,clf__alpha=0.00001,clf__penalty='l2',vect__ngram_range=(1,1))

train result: P=0.951359,R=0.998716,F=0.974463
validate result: P=0.893005,R=0.967067,F=0.928561
```

# test/pipeline.py search space!!
- no enough memory

# 2.0/out_of_core_pipeline.py
- not real out of core, but set pre_batch=3
```
精确模式：
Best score: 0.994
Best parameters set:
	clf__alpha: 1e-06


	clf__penalty: 'l2'
	vect__max_df: 0.5
	vect__ngram_range: (1, 2)

Best score: 0.983
Best parameters set:
	clf__alpha: 1e-06
	clf__n_iter: 80
	clf__penalty: 'l2'
	tfidf__norm: 'l2'
	vect__max_df: 0.5
	vect__max_features: None
	vect__ngram_range: (1, 2)

Best score: 0.995
Best parameters set:
	clf__alpha: 1e-07
	clf__penalty: 'l2'
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)

Best score: 0.962
Best parameters set:
	clf__alpha: 1e-09
	clf__penalty: 'l2'
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)

Best score: 0.991
Best parameters set:
	clf__alpha: 1e-10
	clf__penalty: 'l2'
	vect__max_df: 0.62
	vect__ngram_range: (1, 2)

Best score: 0.967
Best parameters set:
	clf__alpha: 1e-11
	clf__penalty: 'l2'
	vect__max_df: 0.62
	vect__ngram_range: (1, 2)

Best score: 0.965
Best parameters set:
	clf__alpha: 1e-09
	clf__penalty: 'l2'
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)

Best score: 0.987
Best parameters set:
	clf__alpha: 1e-07
	clf__penalty: 'l2'
	tfidf__norm: 'l1'
	tfidf__use_idf: True
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)

Best score: 0.962
Best parameters set:
	clf__alpha: 1e-07
	clf__n_iter: 80
	clf__penalty: 'l2'
	tfidf__norm: 'l1'
	tfidf__use_idf: True
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)

Best score: 0.994
Best parameters set:
	clf__alpha: 1e-09
	clf__penalty: 'l1'
	tfidf__norm: 'l2'
	tfidf__use_idf: True
	vect__max_df: 0.6
	vect__ngram_range: (1, 2)
```

# 2.0/smc.py
```
Classification report for classifier:
             precision    recall  f1-score   support

          0       1.00      0.99      1.00    720000
          1       0.93      0.99      0.96     80000

avg / total       0.99      0.99      0.99    800000


train result: P=0.927053,R=0.989838,F=0.957417

```

