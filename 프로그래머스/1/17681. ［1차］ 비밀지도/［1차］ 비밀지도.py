def solution(n, arr1, arr2):
    answer = []
    binNum = 0
    totalNum = 0
    result = ''
    
    
    for i in range(n):
        binNum1 = int(bin(arr1[i])[2:])+10**n
        binNum2 = int(bin(arr2[i])[2:])+10**n
        totalNum = binNum1 + binNum2
        print(totalNum)
        for j in str(totalNum)[1:]:
            if j != '0':
                result += '#'
            elif j == '0':
                result += " "
        answer.append(result)
        result = ''
            
        
            
            
        
    return answer