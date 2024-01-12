N = int(input())

numbers = list(map(int, input().split()))
sorted_numbers = sorted(list(set(numbers)))
index = {}

for i,j in enumerate(sorted_numbers):
    index[j]=i

#print(index)

for i in numbers:
    print(index[i],end=" ")
print()

