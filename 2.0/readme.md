# reference
- http://scikit-learn.org/stable/auto_examples/index.html#working-with-text-documentss
- http://scikit-learn.org/stable/auto_examples/model_selection/grid_search_text_feature_extraction.html#
- http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer
- http://scikit-learn.org/stable/auto_examples/text/document_classification_20newsgroups.html#example-text-document-classification-20newsgroups-pys

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

