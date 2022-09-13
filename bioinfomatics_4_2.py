import re

gb = open("sequence.protein.gb",'r')

data= gb.readlines()
title = data[0]

prod_1= ''.join(data)
prod_data = prod_1.replace("\n","")

str_data=str(prod_data)


seq_start= int(str_data.index("ORIGIN"))
seq= str_data[(seq_start)+6:]

seq_2= re.sub(r'[0-9]+','',seq)
seq_3= seq_2.replace("'","")
seq_4= seq_3.replace(",","")
seq_f= seq_4.replace(" ","")


print("title: ",title)
print("seq: ", seq_f)

gb.close()