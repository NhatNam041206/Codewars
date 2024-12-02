def sort_array(source_array):
    posOdd=[i for i in range(len(source_array)) if source_array[i]%2]
    odds=sorted([source_array[i] for i in range(len(source_array)) if i in posOdd],reverse=False)
    j=0
    for i in range(len(source_array)):
        if i in posOdd:
            source_array[i] = odds[j]
            j+=1
    return source_array
sort_array([5, 3, 2, 8, 1, 4])