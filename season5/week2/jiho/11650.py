# N = int(input())
# lst = [[0 for i in range(2)]for i in range(N)]
#
# for i in range(N):
#     lst[i][0], lst[i][1] = map(int, input().split())
#
# for j in range(N):
#     for i in range(N-1):
#         if (lst[i][0] > lst[i + 1][0]):
#             lst[i][0], lst[i + 1][0] = lst[i + 1][0], lst[i][0]
#             lst[i][1], lst[i + 1][1] = lst[i + 1][1], lst[i][1]
#         if (lst[i][0] == lst[i + 1][0]):
#             if (lst[i][1] > lst[i + 1][1]):
#                 lst[i][0], lst[i + 1][0] = lst[i + 1][0], lst[i][0]
#                 lst[i][1], lst[i + 1][1] = lst[i + 1][1], lst[i][1]
#
# for i in range(N):
#     print(lst[i][0], lst[i][1])
#

N = int(input())
lst = []
for i in range(N):
    [a, b] = map(int, input().split())
    lst.append([a, b])
lst.sort()
for i in lst:
    print(i[0], i[1])