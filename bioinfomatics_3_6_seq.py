import re

fasta= open("sequence.protein.fasta",'r')

data= fasta.readlines()
prod_1= data[1:]

prod_2= ''.join(prod_1)
prod_3 = prod_2.replace("\n","")
seq= str(prod_3)

fasta.close()
