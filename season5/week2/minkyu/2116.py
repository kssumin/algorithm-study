import sys
input = sys.stdin.readline

N = int(input())
dice_list = []
for _ in range(N):
    dice = (list(map(int, input().split())))
    dice_list.append([[dice[0], dice[5]], [dice[1], dice[3]], [dice[2], dice[4]]])

result = 0
for i in range(1, 7):
    target = i
    tmp_result = 0
    for j in range(N):
        for k in range(3):
            max_num = 0
            if target in dice_list[j][k]:
                first_num, second_num = dice_list[j][k]
                index = [0,1,2]
                index.remove(k)
                if target == first_num:
                    target = second_num
                else:
                    target = first_num

        max_num = max(max_num, max(max(dice_list[j][index[0]]), max(dice_list[j][index[1]])))
        tmp_result += max_num
    result = max(result, tmp_result)

print(result)

