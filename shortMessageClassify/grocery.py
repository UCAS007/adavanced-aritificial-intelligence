# coding=utf-8
from tgrocery import Grocery
# 新开张一个杂货铺（别忘了取名）
grocery = Grocery('sample')
# 训练文本可以用列表传入
train_src = [
    ('0', '名师指导托福语法技巧：名词的复数形式'),
    ('0', '中国高考成绩海外认可 是“狼来了”吗？'),
    ('1', '图文：法网孟菲尔斯苦战进16强 孟菲尔斯怒吼'),
    ('1', '四川丹棱举行全国长距登山挑战赛 近万人参与')
]
grocery.train(train_src)
# 也可以用文件传入（默认以tab为分隔符，也支持自定义）
print grocery.predict('考生必读：新托福写作考试评分标准')
