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

#아래부터 새 코드


nam=len(seq_f)%70


for i in range(0,len(seq_f)//70+1):
    # seq_p= seq_f[i*69:(i+1)69]

    print(seq_f[i*70:(i+1)*70],end='\n')