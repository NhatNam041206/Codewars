'''
#Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O"
-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
'''


def is_solved(board):
    cross=[]
    cZeros=0
    cOnes=0
    cTwos=0
    temp2=[]
    for i in range(3): #Checking if "X" or "O" win
        temp=[]
        temp1=[]
        
        for j in range(3):
            temp.append(board[j][i])
            temp1.append(board[i][j])
            if board[i][j]==0: cZeros+=1
            elif board[i][j]==1: cOnes+=1
            else: cTwos+=1

        if temp1.count(1)==3 or temp.count(1)==3: return 1
        elif temp1.count(2)==3 or temp.count(2)==3: return 2
        
        temp2.append(board[i][i])
    if cZeros>4: return -1
    if temp2.count(1)==3: return 1
    elif temp2.count(2)==3: return 2
    cross.append(temp2)
    temp2=[]
    for i in range(len(board)-1,-1,-1):
        temp2.append(board[i][len(board)-1-i])
    if temp2.count(1)==3: return 1
    elif temp2.count(2)==3: return 2
    if (cZeros<=cTwos or cZeros<=cOnes) and (cTwos-1==cOnes or cOnes-1==cTwos): return 0
    return -1
    
    
    
board = [[0, 0, 1],
         [2, 1, 2],
         [1, 1, 0]]
print(is_solved(board))