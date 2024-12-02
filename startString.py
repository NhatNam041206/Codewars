#Need to do the last part (NOTE)

def firstStage(phrase): #For testing, just return the amount of characters in each initial letter
    s=phrase.lower().split()

    #Take the first letter & sorted them in ascending order
    sortedPhrase=sorted(s, key=lambda x: (x[0], len(x)))
    firstL={}
    startPos=0
    
    for i in range(1,len(sortedPhrase)):
        if sortedPhrase[i][0] not in firstL:
            if sortedPhrase[i][0]!=sortedPhrase[i-1][0]: #just like a breakpoint
                firstL[sortedPhrase[i-1][0]]=[sortedPhrase[j] for j in range(startPos,i)]
                startPos=i

    firstL[sortedPhrase[-1][0]]=[sortedPhrase[j] for j in range(startPos,len(sortedPhrase))]
    
    return firstL

def search(s): #Using BFS search
    level=0
    queqe=[]
    result=[]
    for i in range(len(s[-1])*len(set(''.join(s)))):

        for j in s:
            if len(j)>=level+1:
                if j[level] not in queqe:
                    queqe.append(j[level])
        #Taking the proportional pos
        countC=0
        for j in queqe:
            pos=[]
            count=0
            
            check=False
            for o in range(len(s)):
                if count>level+1:
                    countC+=1
                    check=False
                    break
                if j in s[o] and len(s[o])>=level+1:
                    if s[o].index(j)==level:
                        count+=1
                        pos.append(s[o])
                check=True
            if count<level+1: 
                countC+=1
                check=False
            if count==level+1 and check: result.append(pos)
            
            #print(f'{j}->{pos}')
        level+=1
        if countC==len(queqe) and len(queqe)>1: break
        if len(queqe)!=0: queqe=[]
    return result

def letter(s):
    processed=firstStage(s)
    #print(processed)
    result=[]
    for i in processed:
        if len(processed[i])!=1:
            result+=search(processed[i])
        else:
            result.append(processed[i][0])
    return result

print(letter("a abc abcd abcde hey hello")) # ["abc", "abcd", "abcde", "hello", "hey"]
print(letter("a abc abcd abe hi hello")) #[]
print(letter("Abc aBcd AbcDe")) # ["abc", "abcd", "abcde"]
print(letter("this is all solution")) # ["all", "is", "solution", "this"]
'''
print(letter("only some solutions are answers")) # ["only", "solutions", "some"]
print(letter("nothing is solution neither in string")) # []'''
