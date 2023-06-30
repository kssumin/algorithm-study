import sys
input = sys.stdin.readline
INF = sys.maxsize

def get_solution(index):
    tmp_list = solution[:]
    del tmp_list[index]

    start = 0
    end = len(tmp_list) - 1
    while start <= end:




    return


N = int(input())
solution = list(map(int, input().split()))

if solution[0]*solution[-1] > 0:
    if solution[0] < 0:
        print(solution[-2], solution[-1])
    else:
        print(solution[0], solution[1])
else:
    for i in range(len(solution)):
        get_solution(i)