import sys

cnt = 0
car_cnt = int(sys.stdin.readline())
car_in = {sys.stdin.readline().rstrip() : i for i in range(car_cnt)}
car_out = []
for i in range(car_cnt):
    car = sys.stdin.readline().rstrip()
    car_out.append(car)

for i in range(car_cnt - 1):
    for j in range(i, car_cnt):
        if car_in[car_out[i]] > car_in[car_out[j]]:
            cnt += 1
            break

print(cnt)