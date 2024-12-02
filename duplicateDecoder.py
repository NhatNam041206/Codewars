def duplicate_encode(word):
    word=word.lower().replace('(','*').replace(')','-')
    uniqueOne=list(set(word))
    countWords=[]
    for u in uniqueOne:
        countWords.append(word.count(u))
    for i,count in enumerate(countWords):
        if count==1:
            word=word.replace(uniqueOne[i],'(')
        else:
            word=word.replace(uniqueOne[i],')')
    return word

print(duplicate_encode('abc(()'))