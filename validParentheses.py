def valid_parentheses(paren_str):
    paren_str = list(paren_str)
    startPos=0
    closedCount=paren_str.count(')')
    openCount=paren_str.count('(')
    
    if openCount!=closedCount: return False
    
    for i in range(openCount):
        for j in range(len(paren_str)):
            if paren_str[j]=='(':
                startPos=j
                break

        for j in range(startPos,len(paren_str)):
            if paren_str[j]==')':
                paren_str[j]=''
                paren_str[startPos]=''
                break

    return ')' not in paren_str or '(' not in paren_str  

    
print(valid_parentheses(')((()))('))