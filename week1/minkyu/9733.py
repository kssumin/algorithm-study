import sys
input = sys.stdin.readline

work_bee = []
lines = sys.stdin.readlines()
for line in lines:
    work_bee = work_bee + list(line.split())

work_dict = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}

for work in work_bee:
    if work in work_dict:
        work_dict[work] += 1


work_list = list(work_dict)
work_value = list(work_dict.values())
for i in range(7):
    print("{} {} {:.2f}".format(work_list[i], work_value[i], work_value[i]/len(work_bee)))
print("Total {} 1.00".format(len(work_bee)))
"""
input = sys.stdin.readline

work_bee = []
while 1:
    try:
        work_bee.append(input().rstrip().split())
    except:
        break
        
입력받을 때 이런 식으로 했는데 왜 안되는지 모르겠다..

리스트로 추가돼서 안됐던 거였다..
"""