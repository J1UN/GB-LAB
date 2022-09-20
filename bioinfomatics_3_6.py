import re

fasta= open("sequence.protein.fasta",'r')   #fasta파일 열기

data= fasta.readlines()                     #fasta seq를 readline으로 읽기
prod_1= data[1:]                            #fasta seq의 첫줄(0)인 타이틀 제외

prod_2= ''.join(prod_1)                     #title을 제외한 line들을 list에서 string으로 join
prod_3 = prod_2.replace("\n","")            #string으로 join한 seq의 개행문자 제거
seq= str(prod_3)                            #개행제거한 seq을 str로 반환 

print("title: ",data[0])                    #타이틀출력
print("seq: ",seq)                          #연속된 seq 출력

fasta.close()                               #open한 파일 닫기
