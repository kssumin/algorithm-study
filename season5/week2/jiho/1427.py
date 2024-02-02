str = input()
lst = []
for i in range(len(str)):
    lst.append(int(str[i]))

for i in range(len(lst) - 1):
    max = i
    for j in range(i+1, len(lst)):
        if lst[j] > lst[max]:
            max = j
    lst[i], lst[max] = lst[max], lst[i]

for i in range(len(lst)):
    print(lst[i], end='')

