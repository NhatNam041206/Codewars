def josephus(items,k):
    result=[]
    count=len(items)

    pos=k-1
    check=False
    while count>0:
        while pos>len(items)-1:
            pos-=len(items)
        result.append(items[pos])
        items.pop(pos)
        pos=pos-1+k


        count-=1
    if check: result+=items
    print(result)
        
    


#josephus([1,2,3,4,5,6,7,8,9,10],1)
#print(josephus([1,2,3,4,5,6,7],3))
josephus([True, False, True, False, True, False, True, False, True],9) #[True, True, True, False, False, True, False, True, False]