def findingSuggestedNums(n):
    pairOfNumbers=[]
    for i in range(n):
        for j in range(n):
            suggestedNumbers=sorted([i,j])
            if 0 not in suggestedNumbers and sum(suggestedNumbers)==n and suggestedNumbers not in pairOfNumbers:
                pairOfNumbers.append(suggestedNumbers)
    return pairOfNumbers

def partitions(n):
    sNums=findingSuggestedNums(n)
    temp=[]
    result=[]
    for i in sNums:
        result.append(i)
        for j in i:
            temp.append(findingSuggestedNums(j))
            
    for i in temp:
        for j in i:
            if j not in result:
                result.append(j)
    
    return result
    
print(partitions(5))