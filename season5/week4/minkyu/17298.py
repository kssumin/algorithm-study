import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().rstrip().split()))
# sorted_num_list = sorted(num_list)
# max_num = sorted_num_list[-1]
#
# for i in range(N-1):
#     if num_list[i] < max_num:
#         for j in range(i+1,N):
#             if num_list[j] > num_list[i]:
#                 print(num_list[j], end=" ")
#                 break
#         else:
#             print(-1, end=" ")
#     else:
#         sorted_num_list.pop()
#         max_num = sorted_num_list[-1]
#         print(-1, end=" ")
#
# print(-1)
answer = [-1] * N
stack = []
stack.append(0)
for i in range(1, N):
    while stack and num_list[stack[-1]] < num_list[i]:
        answer[stack.pop()] = num_list[i]
    stack.append(i)

print(*answer)