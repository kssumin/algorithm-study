# BJ 2696 : 중앙값 구하기 / GOLD II / 2628ms

import sys

sys.stdin = open("input.txt", "rt")

t = int(sys.stdin.readline().strip())

for _ in range(t):
    result = []
    
    m = int(sys.stdin.readline().strip())
    
    if m <= 10:
        arr = list(map(int, sys.stdin.readline().strip().split(' ')))
        
    elif 10 < m :
        arr = []
        if m % 10 == 0:
            k = m // 10
            # print('k = ', k)
        elif m % 10 != 0:
            k = m // 10 + 1
            # print('k = ', k)
            
        for _ in range(k):
            arr.extend(list(map(int, sys.stdin.readline().strip().split(' '))))
            # print(arr)
    

    
    for i in range(m):
        if i == 0:
            result.append(arr[i])
        elif i % 2 == 0:
            arr_srt = sorted(arr[0:i+1])
            result.append(arr_srt[i // 2])
    
    # 중앙값의 개수        
    print(int((m + 1) / 2))
    
    len_ = len(result)
    
    if len_ <= 10:
        print(' '.join(list(map(str, result))))
    else:
        for j in range(len_ // 10 + 1):
            print(' '.join(list(map(str, result[10*j:10*(j+1)]))))