import sys
input = sys.stdin.readline

N = int(input())
term = list(map(int, input().split()))
oper = list(map(int, input().split()))
oper_lst = ["+", "-", "*", "/"]
maximum = -1000000000
minimum = 1000000000

def back_tracking(sum, idx, add, sub, mul, div):
    global maximum, minimum
    if idx == N:
        maximum = max(sum, maximum)
        minimum = min(sum, minimum)
        return
    else:
        if add:
            back_tracking(sum + term[idx], idx + 1, add - 1, sub, mul, div)
        if sub:
            back_tracking(sum - term[idx], idx + 1, add, sub - 1, mul, div)
        if mul:
            back_tracking(sum * term[idx], idx + 1, add, sub, mul - 1, div)
        if div:
            back_tracking(int(sum / term[idx]), idx + 1, add, sub, mul, div - 1)

back_tracking(term[0], 1, oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)
