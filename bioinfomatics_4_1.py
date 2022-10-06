import re

gb = open("sequence.protein.gb",'r')

data= gb.readlines()
title = data[0]


str_data1 = ''.join(data)
str_data2 = re.sub(r'[0-9]+', '', str_data1)
str_data3 = str_data2.replace('\n','')
str_data4 = str_data3.replace(' ','')

seq_start= int(str_data4.index("ORIGIN"))
seq= str_data4[(seq_start)+6:]


print("title: ",title)
print("seq: ", seq)

gb.close()
