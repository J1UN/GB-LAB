fasta= open("sequence.protein.fasta",'r')

data= fasta.readlines()

print("The second line is: ",data[1])
fasta.close()
