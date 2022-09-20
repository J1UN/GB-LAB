line_continued = ' ' * 21

CDS_line_flag = False  
CDS_line_list = [] 
for line in open('sequence.nucleotide.gb', 'r'):    # 파일의 각 줄을 모두 읽는다.
    if line.startswith(' ' * 21+'/translation='):   #translation이 나오면 flag true
        CDS_line_flag = True  
        CDS_line_list.append(line.strip())
        continue                                    #공백제거 후, 리스트에 추가. 이후 다음 if문 진행

    if CDS_line_flag is True:                       # flag가 True라면
        if line[0:21] == line_continued:            # line의 0~20번째 글자가 line_continued(공백 21칸)와 일치하면
            CDS_line_list.append(line.strip())      # 해당 linedml 공백과 줄바꿈 제거 후 리스트에 추가

        else:                                       # Translation이 아닌 새로운 칼럼등장 시,
            mola = ''.join(CDS_line_list)           # 리스트를 문자열로 join하여
            print(mola[17:-1])                      # 표지와 따옴표 제거 후,서열만 출력               

            CDS_line_flag = False                   # flag를 False로 초기화
            CDS_line_list = []                      # list를