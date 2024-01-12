# 수가 주어지면 그 수의 각 자리수를 내림차순 정렬
# 출력 : 999998999
# 결과 : 999999998

N = int(input())

print("".join(list(sorted(list((str(N))),reverse=True))))

"""
옛날 답안
N = input()

print(int(''.join((reversed(sorted(N))))))
"""