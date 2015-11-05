# source data
- train.txt: 官方提供的训练数据
- test.txt: 官方提供的测试数据

# trainAndtest.py 源码分析
- splitData.sh: 将train.txt 划分成xaa,xabs
- xab: 程序训练数据
- xab: 程序验证数据

# 测试结果
>precision=0.994838511856
>recall=0.981892464441
>F=0.988323094888

# trainAndWrite.py 源码分析
- train.txt: 训练数据
- test.txt: 验证数据
- result.txt: 分类结果输出
- sample: 分类器保存输出

# 官方数据有误或者readlines的实现的问题
- postprocessing.py 处理train.txt中一条短信对应多行的问题
- 输出post_train.txt 和 post_validate.txt, 但依然无法解决问题
- 因此修改源数据train.txts
- 错误原因：表情等无法解析，或者数据传输错误（多次下载错误一样，因此不太可能是数据传输错误），或者split命令错误(为此实现postprocessing.py，但没有用)
- 然而用 grep -n "" train.txt | wc -l 得出的行数却正确！
- checkText.py 检查划分是否正确！

# trainAndValidate.py
- 使用预处理后的文档进行训练和验证。预处理去掉了短信id

# 学习程序
- grocery.py,train.py