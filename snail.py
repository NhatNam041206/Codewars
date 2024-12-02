def snail(snail_map):
    N=len(snail_map[0])
    result=[]
    pos=0
    count=0
    for pos in range(N):
        for i in range(pos,N-pos): #Left to right
            result.append(snail_map[pos][i])
            count+=1
        if count==N*N: break
        for i in range(1+pos,N-pos):#Down
            result.append(snail_map[i][-1-pos])
            count+=1
        for i in range(N-2-pos,-1+pos,-1):#Right to left
            result.append(snail_map[-1-pos][i])
            count+=1
        if count==N*N: break
        for i in range(N-2-pos,pos,-1): #Up
            result.append(snail_map[i][pos])
            count+=1
    print(result)

snail([[1,2,3],
         [4,5,6],
         [7,8,9]])
snail([[1,2,3],
         [8,9,4],
         [7,6,5]])
snail([[1,2,3,4,5],
       [16,17,18,19,6],
       [15,24,25,20,7],
       [14,23,22,21,8],
       [13,12,11,10,9]])