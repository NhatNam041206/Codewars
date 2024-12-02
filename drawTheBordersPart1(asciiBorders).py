def avoidHoles(data):
    cur=data[0]
    next=[i for i in data if ((i[0]+1==cur[0] or i[0]-1==cur[0]) and i[1]==cur[1]) or ((i[1]+1==cur[1] or i[1]-1==cur[1]) and i[0]==cur[0])]
    result=[data[0]]
    while True:
        if len(next)<=1: 
            return result
        next.pop(0)
        
        cur=next[0]
        result.append(cur)
        for i in data:
            if ((i[0]+1==cur[0] or i[0]-1==cur[0]) and i not in result and i[1]==cur[1]) or ((i[1]+1==cur[1] or i[1]-1==cur[1]) and i not in result and i[0]==cur[0]):
                next.append(i)
def draw_borders(data):
    #Variables setup
    h=[] #horizontal
    v=[] #vertical
    #Sorting the data
    data=sorted(data, key=lambda x: (x[1],x[0]))
    data=[(i[0]-min(list(map(lambda data: data[0], data)))+1, i[1]-min(list(map(lambda data: data[1], data)))+1) for i in data]
    #Taking the height, width for creating the board
    _x,y=list(map(lambda data: data[0], data)),list(map(lambda data: data[1], data))
    board=[[' ']*((min(_x)-1, max(_x)+1)[-1]+1) for i in range(min(y)-1, max(y)+2)]
    
    for i in range(max(y), min(y)-1, -1):
        
        #Taking all the x coordinates
        x=[j[0] for j in data if j[1]==i]
        for j in range(min(x), max(x)+1):          
            
            if (j,i) in data: 
                #Pointers
                checkers=[False]*4 
                for count, pointer in enumerate([(j,i-1), (j+1,i), (j,i+1), (j-1,i)]):  #[up, right, down, left]
                    
                    if pointer not in data: 
                        if count==0: #Up
                            if (j,i-1) in v:
                                board[i-1][j]='+'
                            else: 
                                if board[i-1][j]!='+':
                                    board[i-1][j]='-'

                            h.append((j,i-1))
                            checkers[0]=True
                        
                        elif count==2: #Down
                            if (j,i+1) in v: board[i+1][j]='+'
                            else: 
                                if board[i+1][j]!='+':
                                    board[i+1][j]='-'
                            
                            h.append((j,i+1))
                            if checkers[1] and (j+1,i+1) not in data:
                                board[i+1][j+1]='+'
                            checkers[2]=True

                        elif count==3: #Left
                            if (j-1,i) in h: board[i][j-1]='+'
                            else: 
                                if board[i][j-1]!='+':
                                    board[i][j-1]='|'
                            
                            v.append((j-1,i))
                            if checkers[2] and (j-1,i+1) not in data:
                                board[i+1][j-1]='+'
                            checkers[3]=True
                        
                        else: #Right
                            if (j+1,i) in h: board[i][j+1]='+'
                            else: 
                                if board[i][j+1]!='+':
                                    board[i][j+1]='|'

                            v.append((j+1,i))
                            if checkers[0] and (j+1,i-1) not in data:
                                board[i-1][j+1]='+'
                            checkers[1]=True
                if (checkers[-1] and checkers[0]) and (j-1,i-1) not in data: 
                    board[i-1][j-1]='+'
    

    temp=[(i,j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] in '+-|']
    pos=avoidHoles(temp)
    s=''
    
    for i in range(len(board)-1,-1,-1):
        c=False
        temp=[]
        for g in pos:
            if g[0]==i: temp.append(g[1])
        if len(temp)<1: c=True
        if not c:
            maxX=max(temp)
        
            for j in range(len(board[i])): 
                if (i,j) in pos: s+=board[i][j]
                else: 
                    if j<maxX:
                        s+=' '
            s+='\n'
    return s[:-1]
  
#Test area
test_cases = [
    ('1x1 square', {(1,1)}, '''
+-+
| |
+-+'''),

    ('2x1 rectangle', {(1,1),(2,1)}, '''
+--+
|  |
+--+'''),

    ('1x2 rectangle', {(1,1),(1,2)}, '''
+-+
| |
| |
+-+'''),

    ('2x2 square', {(1,1),(2,1),(1,2),(2,2)}, '''
+--+
|  |
|  |
+--+'''),

    ('4x4 square, with big coords', {(x,y) for x in range(100,104) for y in range(100,104)}, '''
+----+
|    |
|    |
|    |
|    |
+----+'''),

    ('3x2 rectangle', {(1,1),(2,1),(3,1),(1,2),(2,2),(3,2)}, '''\
+---+
|   |
|   |
+---+'''),

    ('5x1 rectangle', {(1,1),(2,1),(3,1),(4,1),(5,1)}, '''\
+-----+
|     |
+-----+'''),

    ('Pyramid', {(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1), (2,2),(3,2),(4,2),(5,2),(6,2), (3,3),(4,3),(5,3), (4,4)}, '''
   +-+
  ++ ++
 ++   ++
++     ++
|       |
+-------+'''),

    ('4x4 square with 2x2 hole', {(0,0),(0,1),(0,2),(0,3),(1,0),(1,3),(2,0),(2,3),(3,0),(3,1),(3,2),(3,3)}, '''
+----+
|    |
|    |
|    |
|    |
+----+'''),

    ('Concave shape', {(1,4),(1,3),(1,2),(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4)}, '''
+-+ +-+
| | | |
| | | |
| +-+ |
|     |
+-----+'''),

    ('Concave shape with narrow niche', {(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(1,2),(2,2),(1,1),(2,1),(3,1),(4,1)}, '''
+------+
|      |
|  +-+-+
|    |
+----+'''),

    ('Snake', {(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(4,3),(3,3),(2,3),(1,3),(1,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(8,4),(8,3),(8,2),(8,1),(9,1),(10,1),(11,1)}, '''
+--------+
|        |
| +---++ |
|     || |
+---+ || +--+
|     ||    |
+-----++----+'''),
    
    ('Touching corners', {(0,1),(1,2),(2,1),(4,3),(3,1),(5,4),(6,4),(7,3),(0,2),(2,2),(1,0),(3,2),(4,4),(7,4),(5,5),(6,5),(0,0),(1,1),(2,0),(3,0),(4,5),(5,3),(7,5),(6,3)}, '''
    +----+
    |    |
    |    |
+---+    |
|    +---+
|    |
|    |
+----+'''),

    ('Test case 1',{(23, 4), (64, 5), (69, 1), (58, 1), (4, 0), (50, -3), (34, 1), (45, 1), (56, 1), (8, 0), (19, 0), (30, 0), (42, 2), (11, -4), (65, -3), (57, 2), (46, 2), (68, 2), (49, -1), (38, -1), (38, -2), (49, -2), (72, 2), (7, 1), (12, -3), (53, -1), (53, -2), (64, -1), (64, -2), (18, 1), (4, 2), (45, 3), (56, 3), (34, 3), (27, -3), (8, 2), (30, 2), (19, 2), (11, -1), (75, 1), (0, -1), (0, -2), (42, 4), (57, 4), (46, 4), (38, 0), (49, 0), (15, -1), (26, -1), (26, -2), (15, -2), (7, 3), (53, 0), (64, 0), (22, 3), (56, 5), (37, 1), (0, 0), (41, 1), (11, 0), (75, 3), (65, 1), (76, 1), (15, 0), (26, 0), (38, 2), (49, 2), (53, 2), (64, 2), (34, -1), (56, -1), (45, -1), (56, -2), (34, -2), (27, 1), (3, 1), (14, 1), (30, -3), (60, -2), (60, -1), (8, -3), (65, 3), (76, 3), (11, 2), (0, 2), (41, 3), (52, 3), (26, 2), (15, 2), (49, 4), (18, -1), (71, 1), (7, -1), (7, -2), (25, 4), (64, 4), (34, 0), (45, 0), (56, 0), (22, -1), (3, 3), (60, 0), (75, -1), (68, 1), (33, 1), (44, 1), (57, 1), (72, 1), (7, 0), (18, 0), (53, -3), (71, 3), (22, 0), (56, 2), (34, 2), (37, -1), (37, -2), (45, 2), (60, 2), (11, -3), (75, 0), (52, -1), (41, -1), (52, -2), (41, -2), (10, 1), (33, 3), (44, 3), (79, 0), (18, 2), (7, 2), (48, 3), (63, 1), (22, 2), (45, 4), (56, 4), (37, 0), (3, -1), (14, -2), (3, -2), (14, -1), (41, 0), (52, 0), (75, 2), (10, 3), (25, 1), (71, -1), (71, -2), (53, 1), (64, 1), (29, 1), (34, -3), (40, 1), (63, 3), (22, 4), (3, 0), (14, 0), (67, 3), (37, 2), (78, 3), (52, 2), (41, 2), (33, -1), (44, -1), (44, -2), (33, -2), (26, 1), (2, 1), (25, 3), (7, -3), (71, 0), (48, -1), (48, -2), (40, 3), (67, -4), (14, 2), (3, 2), (59, 1), (70, 1), (41, 4), (33, 0), (44, 0), (10, -1), (10, -2), (48, 0), (71, 2), (63, -1), (63, -2), (6, 3), (21, 1), (37, -3), (67, -1), (67, -2), (60, 1), (36, 1), (70, 3), (10, 0), (44, 2), (33, 2), (25, -1), (25, -2), (74, 3), (48, 2), (63, 0), (29, -1), (29, -2), (40, -1), (40, -2), (6, 5), (22, 1), (-1, 1), (21, 3), (67, 0), (78, 0), (55, -1), (55, -2), (47, 3), (10, 2), (44, 4), (33, 4), (2, -2), (66, 1), (25, 0), (2, -1), (71, -3), (48, 4), (29, 0), (40, 0), (6, -1), (63, 2), (6, -2), (55, 0), (67, 2), (78, 2), (70, -1), (59, -1), (59, -2), (70, -2), (52, 1), (28, 1), (17, 1), (33, -3), (9, -3), (74, -1), (74, -2), (10, 4), (2, 0), (25, 2), (66, 3), (63, 4), (29, 2), (40, 2), (6, 0), (21, -2), (21, -1), (55, 2), (59, 0), (70, 0), (47, -1), (36, -1), (36, -2), (47, -2), (5, 1), (17, 3), (28, 3), (74, 0), (51, -1), (51, -2), (66, -4), (2, 2), (43, 3), (29, 4), (6, 2), (21, 0), (-1, -1), (-2, -2), (67, -3), (36, 0), (47, 0), (70, 2), (59, 2), (5, 3), (9, 1), (51, 0), (74, 2), (66, -2), (66, -1), (48, 1), (13, 1), (24, 1), (29, -3), (35, 1), (6, 4), (-1, 0), (21, 2), (62, 3), (73, 3), (47, 2), (36, 2), (28, -2), (28, -1), (17, -1), (17, -2), (51, 2), (9, 3), (66, 0), (32, -1), (32, -2), (43, -1), (43, -2), (35, 3), (6, -3), (-1, 2), (39, 3), (-2, 2), (67, 1), (78, 1), (54, 1), (70, -3), (47, 4), (28, 0), (17, 0), (5, -1), (5, -2), (32, 0), (43, 0), (66, 2), (16, 1), (73, -1), (62, -1), (62, -2), (73, -2), (55, 1), (20, 1), (31, 1), (54, 3), (77, -1), (5, 0), (17, 2), (28, 2), (9, -1), (58, 3), (9, -2), (69, 3), (43, 2), (32, 2), (24, -1), (35, -2), (35, -1), (13, -1), (24, -2), (13, -2), (6, 1), (16, 3), (-2, -3), (62, 0), (73, 0), (39, -1), (39, -2), (55, 3), (20, 3), (77, 0), (5, 2), (9, 0), (50, 1), (61, 1), (74, 1), (66, -3), (32, 4), (13, 0), (24, 0), (35, 0), (1, -2), (1, -1), (39, 0), (62, 2), (54, -1), (54, -2), (47, 1), (12, 1), (23, 1), (77, 2), (4, -3), (28, -3), (69, -1), (58, -1), (69, -2), (58, -2), (5, 4), (51, 1), (9, 2), (43, -3), (32, -3), (1, 0), (35, 2), (24, 2), (16, -1), (16, -2), (13, 2), (39, 2), (62, 4), (54, 0), (31, -1), (20, -2), (31, -2), (20, -1), (77, 4), (23, 3), (5, -3), (58, 0), (69, 0), (12, 3), (27, 3), (42, 1), (1, 2), (16, 0), (46, 1), (62, -3), (20, 0), (31, 0), (54, 2), (4, 1), (69, 2), (58, 2), (50, -1), (50, -2), (61, -1), (32, 1), (43, 1), (8, 1), (19, 1), (65, -1), (76, -1), (65, -2), (76, -2), (30, 1), (42, 3), (16, 2), (57, 3), (46, 3), (31, 2), (20, 2), (23, -1), (12, -1), (23, -2), (58, 4), (4, 3), (50, 0), (61, 0), (27, -1), (27, -2), (30, 3), (8, 3), (65, 0), (76, 0), (62, 1), (73, 1), (38, 1), (49, 1), (31, 4), (20, 4), (12, 0), (23, 0), (77, 1), (27, 0), (50, 2), (61, 2), (42, -1), (42, -2), (76, 2), (65, 2), (0, 1), (57, -1), (57, -2), (46, -1), (68, -1), (68, -2), (11, 1), (39, 1), (15, 1), (38, 3), (20, -3), (72, -1), (72, -2), (77, 3), (12, 2), (64, 3), (53, 3), (4, -1), (4, -2), (23, 2), (27, 2), (61, 4), (42, 0), (19, -1), (30, -1), (30, -2), (8, -1), (8, -2), (19, -2), (1, 1), (11, 3), (65, 4), (46, 0), (57, 0), (68, 0), (26, 3), (72, 0)},
     '''
+-----+
|     |
|  +  |
|  |  |
|  |--+
+--+
''')

]

while True:
    c=False
    userInp=input('y for all; name for specific: ').lower()
    if userInp=='y':
        for i in test_cases:
            print(i[0], end='\n')
            print(draw_borders(i[1]))
            print(f'Check: {draw_borders(i[1])==i[-1]}')
        break
    else:
        for i in test_cases:
            if i[0].lower()==userInp:
                print(i[0], end='\n')
                print(draw_borders(i[1]))
                print(f'Check: {draw_borders(i[1])==i[-1]}')
                c=True
    if c:
       break