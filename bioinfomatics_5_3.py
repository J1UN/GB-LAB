import re
import os
from DNA_basecode import Base as base

f= open("sequence.nucleotide.fasta","r")

ffr=f.readlines()                                   #제목입력을 위해 11에서 연 인풋파일 리드라인   

p_seq= ffr[1::]                                     #제목부분 제외하고 읽기
pure_seq=[]                                         #fasta에서 seq를 입력할 빈 리스트
for lines in p_seq:                                 #replace로 개행문자 제거 후, extend로 라인을 pure_seq 리스트에 추가
    pure_seq.extend(lines.replace("\n",""))

str_seq=''.join(pure_seq)                           #pure_seq 리스트를 문자열로 변환('열','열','열'로 저장되어 있기 때문에 문자열로 바꿔서 이어준다.)

#==========================================================================================================

complement={'A':'T','T':'A','C':'G','G':'C'}        #seq을 reverse complement seq으로 바꾸기 위한 딕셔너리
list_comp_seq=[]                                    #상보적 치환을 한 원소들을 넣을 리스트

for n in range(0,len(pure_seq)):                    #pure_seq과 동일한 원소수 적용
    list_comp_seq.append(complement[pure_seq[n]])   #pure_seq의 각 인덱스에 해당하는 문자들을 딕셔너리를 거쳐 키값을 받아 상보적인 서열로 치환 

reverse_comp_seq = ''.join(list_comp_seq)           #문자열로 바꾸어 complement seq 저장

rf1=[]
rf2=[]
rf3=[]
rv_rf1=[]
rv_rf2=[]                                            #triplete code 저장을 위한 리스트
rv_rf3=[]

for i in range(0,len(pure_seq)//3):
    rf1.append(str_seq[3*i:3*(i+1):])
    rf2.append(str_seq[3*i+1:3*(i+1)+1:])
    rf3.append(str_seq[3*i+2:3*(i+1)+2:])
    rv_rf1.append(reverse_comp_seq[3*i:3*(i+1):])
    rv_rf2.append(reverse_comp_seq[3*i+1:3*(i+1)+1:])
    rv_rf3.append(reverse_comp_seq[3*i+2:3*(i+1)+2:])

list_forward1=[]
list_forward2=[]
list_forward3=[]
list_reverse1=[]
list_reverse2=[]
list_reverse3=[]

for rf in range(0,3):
    if rf == 0:
        for n in range(rf,len(pure_seq)//3-rf):
            list_forward1.append(base[rf1[n]])
            list_reverse1.append(base[rv_rf1[n]])

    if rf == 1:
        for n in range(rf,len(pure_seq)//3-rf):
            list_forward2.append(base[rf2[n]])
            list_reverse2.append(base[rv_rf2[n]])

    if rf == 2:
         for n in range(rf,len(pure_seq)//3-rf):
            list_forward3.append(base[rf3[n]])
            list_reverse3.append(base[rv_rf3[n]])

forward1=''.join(list_forward1)
forward2=''.join(list_forward2)
forward3=''.join(list_forward3)
reveres1=''.join(list_reverse1)
reveres2=''.join(list_reverse2)
reveres3=''.join(list_reverse3)

print(forward1,end='    ')
print(forward2,end='    ')
print(forward3,end='    ')

print(str_seq)
print(reverse_comp_seq)

print(reveres1,end='    ')
print(reveres2,end='    ')
print(reveres3,end='    ')
