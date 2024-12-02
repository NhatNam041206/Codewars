
def count_bits(n):
    divided=n//2
    remainder=n%2
    result=[]
    while divided!=0:
        result.append(remainder)
        remainder=divided%2
        divided//=2
    result.append(remainder)
    #result.reverse()
    return result.count(1)
print(count_bits(1234))