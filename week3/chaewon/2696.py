# BJ 2696 : 중앙값 구하기 / GOLD II / 2628ms

import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    
    # 매 테스트 케이스마다 result 초기화
    result = []
    
    m = int(sys.stdin.readline().strip())
    
    # 배열의 길이 m이 10보다 작거나 같으면 한 줄로 입력 받음
    if m <= 10:
        arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    
    # m이 10보다 크면, 여러 줄로 입력 받아야 함
    elif 10 < m :
        
        # arr 선언
        arr = []
        
        # 만약 m이 10의 배수라면 k = m을 10으로 나눈 몫
        if m % 10 == 0:
            k = m // 10
        
        # 만약 m이 10의 배수라면 k = m을 10으로 나눈 몫 + 1
        elif m % 10 != 0:
            k = m // 10 + 1
        
        # k개 줄로 입력받음
        # ex) m = 23
        #     k = 23 // 10 + 1 = 3
        #     3줄로 입력 받음    
        for _ in range(k):
            arr.extend(list(map(int, sys.stdin.readline().strip().split(' '))))

    
    # 입력받은 m을 규칙에 따라 result에 저장
    for i in range(m):
        
        # 첫 번째 인덱스, 즉 arr[0]은 홀수번째 인덱스므로 result에 무조건 저장 
        if i == 0:
            result.append(arr[i])
        # 인덱스값 i가 짝수면, 홀수번째 인덱스에 해당
        elif i % 2 == 0:
            
            # 0부터 i까지의 arr를 정렬하여 새로운 리스트 arr_srt로 저장 
            arr_srt = sorted(arr[0:i+1])
            
            # arr_srt의 중앙값의 인덱스는 항상 i // 2
            # i // 2 인덱스에 해당하는 값을 result에 추가
            result.append(arr_srt[i // 2])
    
    
    
    # 중앙값의 개수 출력
    print(int((m + 1) / 2))
    

    # result의 길이값 저장
    len_ = len(result)
    
    # result의 길이가 10보다 작거나 같으면 한 줄로 출력
    if len_ <= 10:
        print(' '.join(list(map(str, result))))
        
    # result의 길이가 10보다 크면 여러 줄로 출력
    else:
        
        # 28번줄~과 같은 원리로 range값 설정
        # rusult를 slice하여 저장
        # ex) len_ = 12
        #     len_ // 10 + 1 = 12 // 10 + 1 = 2
        #  i) j = 0
        #     print(result[0:10])
        # ii) j = 1
        #     print(result[10:20])
              
        for j in range(len_ // 10 + 1):
            print(' '.join(list(map(str, result[10 * j : 10 * (j + 1)]))))
            
            
'''
NOTE:

처음에 49번줄~50번줄을 구현하지 않아서 오답 처리 되었다.

홀수번째 인덱스일때마다 그전의 요소를 정렬하여 중앙값을 찾아야하는데
정렬하는 과정을 빠뜨렸다!!

사실 애초에 생각을 못했다. 중앙값 = (정렬 후가 아니라 그냥) 가운데 값이라고 생각함

그래도 혼자 이유를 찾고 정답까지 맞혀서 기분이 좋당

'''