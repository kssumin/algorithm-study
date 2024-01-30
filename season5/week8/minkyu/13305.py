import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
gas_station = list(map(int, input().split()))
gas_station = gas_station[:-1]

min_gas = gas_station[0]
result = 0
for i in range(len(gas_station)):
    min_gas = min(min_gas, gas_station[i])
    result += min_gas * distance[i]

print(result)


