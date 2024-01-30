import sys
input = sys.stdin.readline

S = input().rstrip()
count_dict = dict()
count_dict["0"] = 0
count_dict["1"] = 0

flag = S[0]
if flag == '0':
    count_dict["0"] += 1
else:
    count_dict["1"] += 1

for i in range(len(S)):
    if S[i] == flag:
        continue
    else:
        flag = S[i]
        count_dict[flag] += 1

print(min(count_dict["0"], count_dict["1"]))