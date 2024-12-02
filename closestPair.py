import math
a=((2, 2), (2, 8), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9))
def closest_pair(points):
    print(points)
    closest=[]
    distance=1000000
    for a,b in zip(list(points),list(points)):
            distance_t=math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
            if distance_t<distance:
                if distance_t==0 and list(points).count(a)>1:
                    return (a,b)
                    
            elif distance_t!=0:    
                distance=distance_t
                closest=(a,b)             
    
    return closest
closest_pair(a)