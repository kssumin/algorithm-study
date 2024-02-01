N = int(input())

distance = list(map(int,input().split()))
city = list(map(int, input().split()))

total = 0
minimum = city[0]

for i in range(len(city)-1):
    if city[i] < minimum:
        minimum = city[i]

    total += minimum*distance[i]
    
    

print(total)