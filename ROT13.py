def rot13(message):
    inp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    out='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm1234567890'
    dict_mapping = {}
    for i in range(len(out)):
        dict_mapping[out[i]] = inp[i]
    s=''
    for i in message:
        if i in dict_mapping:
            s+=dict_mapping[i]
        else: s+=i
    print(s)
    

rot13('EBG13 rknzcyr')