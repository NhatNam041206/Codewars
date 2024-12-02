def last_digit(n1, n2):
    if n2==0 or n1==0: return 1
    lastD=n1=int(str(n1)[-1])
    lastDs=[lastD]
    for i in range(4):
        lastD*=n1
        lastD=int(str(lastD)[-1])
        if lastD in lastDs: break
        lastDs.append(lastD)
    
    pos=n2%len(lastDs)-1
    print('pos: {}; {} from {}'.format(pos+1,lastDs[pos], lastDs))
    return lastDs[pos]
    

    #return lastD
last_digit(7,last_digit(2,3)) #499942,4
#last_digit(4,2)
#print(last_digit(2 ** 200,2**300))
#print(last_digit(3715290469715693021198967285016729344580685479654510946723 ,68819615221552997273737174557165657483427362207517952651))