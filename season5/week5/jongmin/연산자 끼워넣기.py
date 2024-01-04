# 덧셈 뺄셈 곱셈 나눗셈
# 재귀 함수 + for문
# => 백트래킹


-8 / 3

def dfs():
    global tmp, N, step, exp

    if step > N-1:
        
        result.append(tmp)

    for i in range(4):
        if operators[i]>0:

            operators[i] -= 1

            if i==0:
                tmp += numbers[step]
                
            elif i==1:
                tmp -= numbers[step]
                
            elif i==2:
                tmp *= numbers[step]
                
            elif i==3:
                # 음수일 때 // 연산을 해버리면
                # -1 // 3 -> -1 이기 때문이에 오류가 발생
                if tmp >= 0:
                    r.append(tmp%numbers[step])
                    tmp = tmp // numbers[step]
                else:
                    r.append(-(-tmp % numbers[step]))
                    tmp = (-tmp//numbers[step]) * -1
                

            # operator이 1보다 클 경우에 다음 단계로 시작
            step += 1
            dfs()
            step -= 1

            if i==0:
                tmp -= numbers[step]
                
            elif i==1:
                tmp += numbers[step]
                
            elif i==2:
                tmp //= numbers[step]
                
            elif i==3:
                tmp *= numbers[step]
                tmp += r.pop()
                
            operators[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

exp = str(numbers[0])
r = []
step = 1
tmp = numbers[0]
result = []

dfs()

print(max(result))
print(min(result))