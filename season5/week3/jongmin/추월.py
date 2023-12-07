#2002번
N = int(input())

daegeun = {}
youngsik = {}
cars = []
cnt = 0


for i in range(N):
    car = input().rstrip()
    daegeun[car] = i+1
    cars.append(car)
    

for i in range(N):
    youngsik[input()] = i+1

#print(cars)
for i in range(len(cars)):
    for j in range(len(cars)):
        # 상대적인 순서가 처음과 같다면 추월하지 않은 것이다.
        #print(f"car[{i}] = {cars[i]}, car[{j}]={cars[j]}")
        if (daegeun[cars[i]] > daegeun[cars[j]] and youngsik[cars[i]] < youngsik[cars[j]]):
            cnt += 1
            break

print(cnt)
# a b c d e
# e a b c d
# e b c d a
# 