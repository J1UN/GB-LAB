gb = open("sequence.protein.gb",'r')

data= gb.readlines()
title = data[0]
str_data=str(data)

seq_start= int(str_data.index("ORIGIN"))
seq= str_data[(seq_start)+6:]


print("title: ",title)
print("seq: ", seq)

gb.close()