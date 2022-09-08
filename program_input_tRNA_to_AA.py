def tRNA_transcriptor():

    base={'UUU':'F','UUC':'F','UUA':'L','UUG':'L', 'CUU':'L','CUC':'L','CUA':'L','CUG':'L','AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V'
      , 'GUC':'V','GUA':'V','GUG':'V','UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCA':'P','CCG':'P','ACU':'T'
      , 'ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A','UAU':'Y','UAC':'Y','UAA':'STOP','UAG':'STOP','UGA':'STOP',
      'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'D','GAG':'E','UGU':'C'
      , 'UGC':'C','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G'
      , 'GGG':'G'}

    s_origin= input("sequence: ")


    ind_met=s_origin.index("AUG")

    l_seq=int((len(s_origin)-int(ind_met))/3)

    list_s=[]

    for i in range(l_seq):
        list_s.append(s_origin[ind_met+3*i:ind_met+(3*(i+1)):])

    s= str(list_s)




    print("amino acid sequence: ", end="")
    for i in list_s:
        aa=(base[i])
        if aa =='STOP':
            break
        else:
            print(aa, end='')


tRNA_transcriptor()
