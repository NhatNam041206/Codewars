def rotate(matrix, direction): #clockwise and counterclockwise
    M=len(matrix)
    N=len(matrix[0])
    result=[]
    temp=[]
    if direction=='clockwise':
        for i in range(N):
            temp=[]
            for j in range(M-1,-1,-1):
                temp.append(matrix[j][i])
            result.append(temp)
    else:
        for i in range(N-1,-1,-1):
            temp=[]
            for j in range(M):
                temp.append(matrix[j][i])
            result.append(temp)
        
    return result

rotate([[1,2,3],
        [4,5,6],
        [7,8,9]], 'clockwise')