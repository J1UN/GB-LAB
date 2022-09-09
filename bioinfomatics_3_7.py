from bioinfomatics_3_6_seq import seq 

aa_num = int(input("Position: "))

aa_seq= seq[aa_num]+seq[aa_num+1]+seq[aa_num+2]


print("Three amino acids: ",aa_seq)
