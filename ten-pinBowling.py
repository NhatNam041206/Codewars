def bowling_score(frames):
    dict={'0':0,'1': 1, '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'X':10}
    frames=frames.split(' ')
    totalScore=0
    for i in range(len(frames)):
        
        if 'X' in frames[i] and len(frames[i])!=3: #Checking when Strike
            if len(frames[i+1])>=2:
                if '/' not in frames[i+1]:
                    totalScore+=10+dict[frames[i+1][0]]+dict[frames[i+1][1]]
                else: 
                    totalScore+=10+10

            elif len(frames[i+1])<2: #Only when next frame is Strke
                totalScore+=10+10+dict[frames[i+2][0]]

        elif '/' in frames[i] and len(frames[i])<3: #Checking when Spare
            totalScore+=10+dict[frames[i+1][0]]
        
        elif len(frames[i])>=3: #This frame is the 10th frame
            if '/' == frames[i][1]: #When Spare
                totalScore+=10+dict[frames[i][-1]]
            elif 'X' == frames[i][0] and '/' in frames[i] and frames[i].count('X')<2: #When Strike and the next round is Spare
                totalScore+=10*frames[i].count('X')+10+dict(frames[i][-1])
            elif frames[i].count('X')==2:
                if '/' in frames[i]:
                    totalScore+=30
                else:
                    totalScore+=20+dict[frames[i][-1]]
            else: totalScore+=30
            break

        else:
            totalScore+=dict[frames[i][0]]+dict[frames[i][1]]
    return totalScore
s='5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5'
print(bowling_score(s.replace('-','0')))