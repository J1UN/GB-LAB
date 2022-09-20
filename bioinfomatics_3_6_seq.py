import re

fasta= open("sequence.protein.fasta",'r')
data= fasta.readlines()

title= data[0]
prod_1= data[1:]

prod_2= ''.join(prod_1)
seq = prod_2.replace("\n","")

fasta.close()
