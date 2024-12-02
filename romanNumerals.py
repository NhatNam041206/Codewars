def solution(n):
    romanNumerals1=['I', 'X', 'C', 'M']
    romanNumerals5=['V', 'L', 'D']
    specialNumbers=[4,9]
    n=str(n)
    pos=0
    result=''
    for i in range(len(n)):
        temp=''
        numberTaken=int(n[i])
        if  numberTaken in specialNumbers: #Only on minus situations
            if numberTaken==4:
                pos=len(n)-i-1
                result+=romanNumerals1[pos]
                result+=romanNumerals5[pos]
            
            else:     
                pos=len(n)-i-1
                result+=romanNumerals1[pos]+romanNumerals1[pos+1]
                

        else: #General plus
            if numberTaken>5:
                pos=len(n)-i-1
                result+=romanNumerals5[pos]
                for j in range(numberTaken-5):
                    result+=romanNumerals1[pos]
            else:
                pos=len(n)-i-1
           
                if numberTaken==5:
                    result+=romanNumerals5[pos]
           
                else:
                    for j in range(numberTaken):
                        result+=romanNumerals1[pos]
    return result
print(solution(2024))
