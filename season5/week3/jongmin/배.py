N = int(input())
crane = list(map(int,input().split()))
M = int(input())
boxes = list(map(int,input().split()))
task = {}

crane.sort()
boxes.sort()

for i in crane:
  task[i] = 0

# 크레인으로 옮길 수 있는 최대 무게가
# 박스의 최대 무게 보다 크거나 같아야 옮길 수 있다.
if max(crane) >= max(boxes):
  i = 0
  j = 0
  while j<M:
    if 

  print(len(max(task,key=lambda x:len(x))))

# 그렇지 않은 경우라면 못 옮기는 상황이므로 -1
else:
  print(-1)

# 넣을 수 있는 가장 작은 크레인에 넣기
# task가 가장 적은 크레인에 넣기