from bioinfomatics_3_6_seq import seq 

aa_num = int(input("Position: ")) -1               # 아미노산의 위치 입력

aa_seq= seq[aa_num:aa_num+3]                    # 입력 위치로부터 3번째까지의 문자열(아미노산)을 aa_seq에 저장


print("Three amino acids: ", aa_seq)             
