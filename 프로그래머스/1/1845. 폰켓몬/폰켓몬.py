def solution(nums):
    answer = 0
    numsDict = {}
    
    for i,num in enumerate(nums):
        if num in numsDict:
            numsDict[num] += 1
        else:
            numsDict[num] = 1
    
    print(len(numsDict))
    if len(numsDict) > (len(nums)/2):
        return (len(nums)/2)
    else:
        return len(numsDict)
    

