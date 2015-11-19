#! encoding=utf-8
import sys
import codecs
import re
import csv
import sys

reload(sys)

#sys.setdefaultencoding('utf-8')
raw_file='/home/wangjianfei/git/data/test.txt'
output_file='after_pre_process.txt'
raw_file=codecs.open(raw_file,'r','utf-8')
data=raw_file.readlines()
i=0
print('start')
logn_s=''
result=[]
for line in data:
	i=i+1
	 
	#split_datas=re.split('\n',line)
	#line=line.replace('\n','')
	split_datas=line.split('\t')
	if(len(split_datas)<3):
		long_s=long_s.replace('\r\n','')+''.join(split_datas)
		continue
	else:
		if(i!=1):
			#print(long_s.encode('utf-8'))
			result.append(long_s)
			long_s=''
			
	temp=split_datas[0]+'\t'+split_datas[1]+'\t'
	del split_datas[0]
	del split_datas[0]
	temp_s=''.join(split_datas)
	temp_s=temp+temp_s
	long_s=temp_s
fileout=codecs.open(output_file,'w','utf-8')
fileout.writelines(result) 
raw_file.close()

 