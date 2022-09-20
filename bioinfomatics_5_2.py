import re
import os

f= open("sequence.nucleotide.fasta","r")

ffr=f.readlines()                               #제목입력을 위해 11에서 연 인풋파일 리드라인   

p_seq= ffr[1::]                                 #제목부분 제외하고 읽기
pure_seq=[]                                     #fasta에서 seq를 입력할 빈 리스트
for lines in p_seq:                             #replace로 개행문자 제거 후, extend로 라인을 pure_seq 리스트에 추가
    pure_seq.extend(lines.replace("\n",""))

str_seq=''.join(pure_seq)                       #pure_seq 리스트를 문자열로 변환('열','열','열'로 저장되어 있기 때문에 문자열로 바꿔서 이어준다.)

base={'TTT':'F','TTC':'F','TTA':'L','TTG':'L', 'CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V'
      , 'GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCA':'P','CCG':'P','ACT':'T'
      , 'ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','TGA':'*',
      'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'D','GAG':'E','TGT':'C'
      , 'TGC':'C','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G'
      , 'GGG':'G'}
#DNA seq 코드와 아미노산서열의 딕셔너리 


codon=[]                                            #triplete code 저장을 위한 리스트
for i in range(1,len(pure_seq)//3+1):               #i의 범위는 pure_seq의 염기 수
        codon.append(str_seq[3*(i-1):(3*(i)):])     #codon리스트에 str_seq를 인덱스 '012','345'순으로 추가 ※.append(시작점:종료점:스텝)


for i in range(1,len(pure_seq)//60+2):              #i의 범위는 전체seq을 60bp단위로 끊어 출력했을 때의 열 개수 

    if i<(len(pure_seq)//60+1):                 #i의 열이 마지막 코드가 있는 열이 아닌 경우     
        print(str_seq[60*(i-1):60*(i)])             #i가 1부터시작하지만 str_seq의 번호는 0부터이므로 0~59,60~119까지의 코드 출력 ※문자열[이상:미만]
    
        for n in range(20*(i-1),20*(i)):            #아미노산 seq은 dna seq의 1/3배 이므로 60/3=20을 배수로 곱한다
            if n==20*(i)-1:                         #n이 해당 seq의 마지막 번호일 경우 base딕셔너리에서 키값반환하고 줄바꿈
                print(base[codon[n]],end='\n')
            else:                                   #n이 마지막 번호가 아니면 키값반환후 줄바꾸지않고 '  '(스페이스*2)를 end값에 부여
                print(base[codon[n]],end='  ')
#==================================================================================

    else:                                       #i의 열이 마지막 서열인 경우
        print(str_seq[60*(i-1):])                   #dna seq의 마지막열의 처음부터 끝까지 출력

        for n in range(20*(i-1),20*(i-1)+(len(pure_seq)%60)//3):     
                                                    #마지막 60개의 시작지점부터 나머지개수에서 3을 나눈것까지 범위설정(시작점,시작점+나머지//3)

            print(base[codon[n]],end='  ')          #마지막이므로 줄바꿈은 하지 않고 끝낸다.
