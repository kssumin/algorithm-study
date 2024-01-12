import sys
def FindSideMax(dice_lst, bottom):
    for i in range(6):
        if dice_lst[i] == bottom:
            break
    if i == 0:
        return (dice_lst[5], max(dice_lst[1], dice_lst[2], dice_lst[3], dice_lst[4]))
    elif i == 1:
        return (dice_lst[3], max(dice_lst[0], dice_lst[2], dice_lst[4], dice_lst[5]))
    elif i == 2:
        return (dice_lst[4], max(dice_lst[0], dice_lst[1], dice_lst[3], dice_lst[5]))
    elif i == 3:
        return (dice_lst[1], max(dice_lst[0], dice_lst[2], dice_lst[4], dice_lst[5]))
    elif i == 4:
        return (dice_lst[2], max(dice_lst[0], dice_lst[1], dice_lst[3], dice_lst[5]))
    elif i == 5:
        return (dice_lst[0], max(dice_lst[1], dice_lst[2], dice_lst[3], dice_lst[4]))

dice_cnt = int(sys.stdin.readline())
dice_lst = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(dice_cnt)]
max_sum = 0

for i in range(1, 7):
	new_bottom = i
	sum = 0
	for j in range(dice_cnt):
		new_bottom, ret = FindSideMax(dice_lst[j], new_bottom)
		sum += ret
	if max_sum < sum:
		max_sum = sum
print(max_sum)