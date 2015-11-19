#1.0
- preprocessing.py 将../data/rawtrain.txt 按4:1划分成train.txt 及 validate.txt
- train.py 从../shortMessageClassify/trainAndValidate.py 中复制并更改得到
- validate.py 从../shortMessageClassify/trainAndValidate.py 中复制后加错误输出得到
- test.py 类似validate.py，并将分类结果输入../data/upload.csv
- ../data 包含要用到的数据train.txt test.txt validate.txt rawtrain.txt(原始数据) rawtest.txt(原始数据)
- ../output 用于输出result.txt,upload.csv
- error.log 从../output/result.txt 复制得到

# error.log
- FN: false negtive + 原文本 
- FP: false postive + 原文本

# tree .
```
.
├── error.log
├── preprocessing.py
├── preprocessing.pyc
├── readme.md
├── readme.md~
├── sample
│   ├── converter
│   │   ├── class_map.config.pickle
│   │   ├── feat_gen.config.pickle
│   │   └── text_prep.config.pickle
│   ├── id
│   └── learner
│       ├── idf.pickle
│       ├── liblinear_model
│       └── options.pickle
├── test.py
├── train.py
├── validate.py
└── version1.0
    ├── converter
    │   ├── class_map.config.pickle
    │   ├── feat_gen.config.pickle
    │   └── text_prep.config.pickle
    ├── id
    └── learner
        ├── idf.pickle
        ├── liblinear_model
        └── options.pickle
```
# tree ..
```
..
├── data
│   ├── rawtest.txt
│   ├── rawtrain.txt
│   ├── test.txt
│   ├── train.txt
│   └── validate.txt
├── output
│   ├── result.txt
│   └── upload.csv
├── readme.md
├── shortMessageClassify
│   ├── checkText.py
│   ├── grocery.py
│   ├── postprocessing.py
│   ├── post_train.txt
│   ├── post_validate.txt
│   ├── preprocess_1119.py
│   ├── readme.md
│   ├── sample
│   │   ├── converter
│   │   │   ├── class_map.config.pickle
│   │   │   ├── feat_gen.config.pickle
│   │   │   └── text_prep.config.pickle
│   │   ├── id
│   │   └── learner
│   │       ├── idf.pickle
│   │       ├── liblinear_model
│   │       └── options.pickle
│   ├── splitData.sh
│   ├── test.txt
│   ├── trainAndtest.py
│   ├── trainAndValidate.py
│   ├── trainAndWrite.py
│   ├── train.py
│   ├── train.txt
│   ├── train.txt~
│   ├── xaa
│   └── xab
└── shortMessageClassify1.0
    ├── error.log
    ├── preprocessing.py
    ├── preprocessing.pyc
    ├── readme.md
    ├── readme.md~
    ├── sample
    │   ├── converter
    │   │   ├── class_map.config.pickle
    │   │   ├── feat_gen.config.pickle
    │   │   └── text_prep.config.pickle
    │   ├── id
    │   └── learner
    │       ├── idf.pickle
    │       ├── liblinear_model
    │       └── options.pickle
    ├── test.py
    ├── train.py
    ├── validate.py
    └── version1.0
        ├── converter
        │   ├── class_map.config.pickle
        │   ├── feat_gen.config.pickle
        │   └── text_prep.config.pickle
        ├── id
        └── learner
            ├── idf.pickle
            ├── liblinear_model
            └── options.pickle
```
