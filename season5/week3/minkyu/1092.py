import sys
input = sys.stdin.readline

N = int(input())
crane_list = sorted(list(map(int, input().rstrip().split())))
M = int(input())
box_list = sorted(list(map(int, input().rstrip().split())))
count = 0
box_len = len(box_list)
is_movable = True
while box_list:
    if crane_list[-1] < box_list[-1]:
        is_movable = False
        break

    for i in range(len(crane_list)):
        index = box_len - 1
        if index >= 0 and crane_list[i] < box_list[0]:
            continue
        while 1:
            if index < 0:
                break
            if box_list[index] <= crane_list[i]:
                box_list.pop(index)
                box_len -= 1
                break
            else:
                index -= 1
    count += 1


if is_movable:
    print(count)
else:
    print(-1)
