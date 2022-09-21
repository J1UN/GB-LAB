import re

gb = open("sequence.protein.gb",'r')

data= gb.readlines()
title = data[0]


str_data=''.join(data)
str_data2= str_data.relace('\n','')
seq_start= int(str_data.index("ORIGIN"))
seq= str_data2[(seq_start)+6:]


print("title: ",title)
print("seq: ", seq)

gb.close()
