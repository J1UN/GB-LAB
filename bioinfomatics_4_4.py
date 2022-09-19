import os
from socket import if_indextoname
import Bio.SeqIO as SeqIO

in_title= input("Enter input file: ")
out_title=input("Enter output file: ")

print("Option-1) Read a FASTA format DNA sequence file and make a reverse sequence")
print("Option-2) Read a FASTA format DNA sequence file and make a reverse compleme")
print("Option-3) Convert GenBank format file to FASTA format file")

op_=(input("Select the option: "))

try:
    if int(op_)== 1 or 2:
        in_file_op= open(in_title,'r')      #인풋 파일 열기
        out_file_op= open(out_title,'w')    #아웃풋 파일열기
    
        data_title_r=in_file_op.readlines() #제목입력을 위해 11에서 연 인풋파일 리드라인   
        data_title=data_title_r[0]          #입력할 제목 추출

        out_file_op.write(data_title)       #아웃풋 파일에 제목입력

#data= in_file_op.read()             #데이터 추출을 위해 인풋파일 열고 읽기
        p_seq= data_title_r[1::]                  #제목부분 제거
        pure_seq=[]
        for lines in p_seq:
            pure_seq.extend(lines.replace("\n",""))

        str_seq=''.join(pure_seq)                   #문자열로
        rev_seq=list(str_seq)[::-1]

        rev_seq_s=''.join(rev_seq) 

        if int(op_)==1:
            out_file_op.write(rev_seq_s)        #리버스 시퀀스 입력

            in_file_op.close()
            out_file_op.close()

#op2 정보가공
        elif int(op_)==2:
            rev_comp=[]
            rev_comp_table={'G':'C', 'A':'T','C':'G','T':'A'}
                                    #상보서열 변환을 위해 값부여
            for i in rev_seq_s:               #리버스시퀀스의 서열 변환
                rv_base=rev_comp_table[i]
                rev_comp.append(rv_base)
                rev_comp_s=''.join(rev_comp)

            out_file_op.write(rev_comp_s)

#========================[bio를 import안한 경우]========================
# elif op==2:
#    rev_comp=[]
#    rev_comp_table={'G':'C', 'A':'T','C':'G','T':'A'}
                                    #상보서열 변환을 위해 값부여
#    for i in rev_seq:
#        rev_comp.append(rev_comp_table[i])
                                    #상보서열로 변환
        
#    out_op2=str(rev_comp)           #상보서열을 문자열로
#    out_fasta.write(out_op2)        #상보서열 입력
#=======================================================================


#op3 정보가공
    if int(op_)==3:
        in_gb= SeqIO.parse(in_title,"gb")
        SeqIO.write(in_gb, out_title, "fasta")

        in_file_op.close()
        out_file_op.close()

    else:
        print("Input is wrong number(1~3).")

except ValueError as e:
    print(e)