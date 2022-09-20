import re
import os

f= open("sequence.nucleotide.fasta","r")

ffr=f.readlines() #제목입력을 위해 11에서 연 인풋파일 리드라인   

p_seq= ffr[1::]                  #제목부분 제거
pure_seq=[]
for lines in p_seq:
    pure_seq.extend(lines.replace("\n",""))

str_seq=''.join(pure_seq)

for i in range(0,len(pure_seq)//3):
    print(str_seq[3*i], end='')
    print(str_seq[3*i+1],end='')
    print(str_seq[3*i+2])
