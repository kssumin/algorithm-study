import sys
input = sys.stdin.readline

N, M = map(int, input().split())
input_list = []
for i in range(N):
    input_list.append(list(input().rstrip()))

max_length = 0
for i in range(N):
    for j in range(M):
        length = min(M-j-1, N-i-1)
        while length > 0:
            if length <= max_length:
                break
            if input_list[i][j] == input_list[i + length][j] and input_list[i][j] == input_list[i][j + length] and input_list[i][j] == input_list[i + length][j + length]:
                max_length = max(max_length, length)
            length -= 1

print((max_length+1)**2)


"""
for문 만들기
빅오 계산
O(n) = 1억
O(n^2) = 1만
O(n^3) = 500
O(n^4) = 20
"""