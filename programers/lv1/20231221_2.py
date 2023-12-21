def solution(n, m, section):
    count = 1
    
    flag = section[0] + m - 1
    while section:
        if section[0] <= flag:
            section.pop(0)
            
        else:
            count += 1
            flag = section[0] + m - 1
    
    return count

print(solution(8, 4, [2, 3, 6]))
            