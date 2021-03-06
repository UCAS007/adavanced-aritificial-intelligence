# 高级人工智能
- 垃圾短信分类 shortMessageClassify
- 京东图片分类 
- 华院数据中文地址魔方大赛
- 判决书中的金额项提取

## 数据集及项目介绍
- [中国好创意大赛](http://www.wid.org.cn/project/2015ccf/index.php)
- [百度云数据集](http://pan.baidu.com/s/1sjAD6Z7)

---

#高级人工智能调研

##垃圾短信的识别
- 参考：基于文本处理的垃圾短信识别
- 参考：基于svm的垃圾短信识别
- 基本思路：中文分词+机器学习
- 希望用python，容易切换到deep learning
- c++ 的机器学习库不一定能编译安装成功，有不少麻烦，win32+mingw32,而mingw有bug32

###中文分词库
- 参考：[中文分词](http://www.zhihu.com/question/19578687) [python 中文分词](http://www.zhihu.com/question/20294818)
- Gate: general architecture for text engineering
- Lucene(java):
- jieba,scseg,genius,smallseg,pynlpir(python):

###文本分类
- 贝叶斯文本分类 [csdn cowboy_wz](http://blog.csdn.net/chl033/article/details/5449206)
- 文本分类示例(python,附benchmark) [csdn Rachel-Zhang](http://blog.csdn.net/abcjennifer/article/details/23615947)
- [TextGrocery+jieba](https://github.com/2shou/TextGrocery)(python)
- [weka 文本分类](http://datamining.xmu.edu.cn/~zq/dmkd/text.htm)(java)
- [LibShortText]<[TextGrocery]
- [libsvm](http://shiyanjun.cn/archives/548.html)(java)

##华院数据中文地址魔方大赛

###数据
```
###输入数据格式
序号,源地址
1,北京朝阳区北四环东路108号千鹤家园(华堂商场后身)5乙楼1101室
2,北京朝阳区白家庄东里42号中轻集团院内D-life礼堂(北京青年报大厦对面中轻集团院内)
3,"北京丰台区紫芳园4区首开璞瑅1号楼115号底商(近刘家窑地铁站,方庄桥,二中院,四中分校,东方医院)"
4,北京朝阳区百子湾路5号沿海赛洛城有条斜街2条下沉花园((近古董钢琴店))
5,北京朝阳区建外soho西区12号楼505(清华CBD附属小学)
6,北京丰台区马官营南路6号院中景未山赋3号楼2单元1702

###输出数据格式
序号,源地址,省,地市,县区,街镇乡,路,路号,楼号,单元号,户号,备注
96383,广州市增城区增城凤凰城内,广东省,广州市,增城区,null,null,增城凤凰城,null,null,null,null
96809,广州市白云区永平街集显1号,广东省,广州市,白云区,null,永平街,集显1号,null,null,null,null
182953,靖江其他地区江州路任景村(重庆烧鸡公旁),江苏省,泰州市,靖江市,null,江州路,任景村,null,null,null,重庆烧鸡公旁
36354,成都武侯区南浦中路1号附3号,四川省,成都市,武侯区,null,南浦中路,1号,null,null,null,附3号
171205,重庆渝北区龙溪街道松牌路142号,重庆市,重庆市辖区,渝北区,龙溪街道,松牌路,142号,null,null,null,null
```

###解决思路
- 收集全国地址数据库，在此基础上进行分词，地址的形式有限，因此问题可以简化
- 简化：地址的表达语法相对简单，有许多明显的标志如：校，医院，地铁站，桥等。。。



##京东商品图片分类
- 图片有39类，大小为256 x 256的彩色图像
- 可以用opencv等库提取特征，再用svm等学习算法进行分类


##判决书中的金额项提取
- 数据
```
documentid,document
1014150,"据此，依照《中华人民共和国担保法》第十八条，最高人民法院关于适用《中华人民共和国担保法》若干问题的解释第二十三条及《中华人民共和国民事诉讼法》第一百七十条第一款第（二）项及第一百七十五条之规定，判决如下：
一、维持上海市浦东新区人民法院（2014）浦民六（商）初字第6604号民事判决第一项，即被上诉人上海三毛进出口有限公司应于本判决生效之日起十日内归还上诉人中信银行股份有限公司上海分行押汇金额9，644，014.96美元；
二、维持上海市浦东新区人民法院（2014）浦民六（商）初字第6604号民事判决第二项，即被上诉人上海三毛进出口有限公司应于本判决生效之日起十日内偿付上诉人中信银行股份有限公司上海分行至2014年5月23日止的逾期付款利息191，729.26美元，并自2014年5月24日起至实际清偿日止分别按约定利率偿付逾期利息，其中6，636，910.96美元按1.905%计算、1，531，104美元按1.303%计算、1，476，000美元按1.304%计算；
三、撤销上海市浦东新区人民法院（2014）浦民六（商）初字第6604号民事判决第三项；
四、被上诉人上海三毛企业（集团）股份有限公司对被上诉人上海三毛进出口有限公司上述还款义务在人民币6，000万元最高额内承担连带担保责任。被上诉人上海三毛企业（集团）股份有限公司承担全部责任后可依法向被上诉人上海三毛进出口有限公司追偿。
负有金钱给付义务的当事人如未按本判决指定的期间履行给付义务，应当按照《中华人民共和国民事诉讼法》第二百五十三条之规定，加倍支付迟延履行期间的债务利息。"
```
