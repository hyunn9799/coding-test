def solution(name, yearning, photo):
    answer = []
    nameDict = {}
    total = 0
    
    for i,char in enumerate(name):
        nameDict[char] = yearning[i]
    
    print(nameDict)
    
    for p in photo:
        for c in p:
            if c in nameDict:
                total += nameDict[c]
        answer.append(total)
        total = 0
        
    
    return answer