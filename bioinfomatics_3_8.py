from bioinfomatics_3_6_seq import seq 


while(True):                            #서치 AA 반복
    target = input("Searching for: ")   #서치 AA입력칸

    index = -1                          #인덱스가 0번부터 시작하므로 (*)
    num_list=[]                         #AA 인덱스를 입력할 리스트
    
    if target == "XXX":                 #XXX입력 시, 서치 반복문  종료위해 앞에 배치
        print("Okay, I will stop.")
        break
    
    else:                               #XXX가 아닐 시 반복수행
        while(True):
            index = seq.find(target, index + 1)
            
            if index == -1:             #index가 -1인 경우 값이 없는 것이므로 중지
                break

            num_list.append(index)      #매 검색마다 index를 리스트에 추가

        
        result= ', '.join(str(s) for s in num_list)
                                        #서치 반복문 밖에서 리스트를 문자열로 변환


    print("Found at: ",result)          #인풋 반복문 안에서 결과값 도출


