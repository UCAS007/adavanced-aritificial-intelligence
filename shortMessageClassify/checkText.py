# coding=utf-8
import codecs

post_file=codecs.open('post_train.txt','r','utf-8')
post_lines=post_file.readlines()

print post_lines.__len__()