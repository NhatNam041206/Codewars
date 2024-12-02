def max_sequence(array):
    ms=tp=array[0]
    for i in range(1,len(array)-1):
        tp=max(array[i],array[i]+tp)
        if tp>ms:
            ms=tp
    return ms


print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))#155