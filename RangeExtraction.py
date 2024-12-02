def solution(args):
    s='' #Solution
    temp=[]
    for i in range(1,len(args)):

        if args[i-1]==args[i]-1:
            temp.append(args[i-1])
            temp.append(args[i])
        else:
            temp=sorted(list(set(temp)))
            if len(temp)>2:
                s+=str(temp[0])+'-'+str(temp[-1])+','
            
            else:
                if len(temp)>0:
                    s+=','.join(map(str,temp))+','
                else: s+=str(args[i-1])+','
            temp=[]
    
    if len(temp)>2:
        s+=str(temp[0])+'-'+str(temp[-1])
    elif len(temp)>=1:
        s+=','.join(map(str,temp))
    else: 
        tempS=s.split(',')
        if tempS[-1]!=args[-1]: 
            s+=str(args[-1])
        else: s=s[:-1]
    return s
solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20,22,24,25,26,28]) # Output:'-6,-3-1,3-5,7-11,14,15,17-20'
solution([-3,-2,-1,2,10,15,16,18,19,20])