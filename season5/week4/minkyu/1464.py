import sys
input = sys.stdin.readline

letter = list(input().rstrip())
is_reverse = False
reverse_index = []
for i in range(len(letter) - 1, 0, -1):
    for j in range(i-1, -1, -1):
        if is_reverse:
            if ord(letter[i]) >= ord(letter[0]) :
                is_reverse = not is_reverse
                reverse_index.append(i)
                break
        else:
            if ord(letter[i]) <= ord(letter[0]):
                is_reverse = not is_reverse
                reverse_index.append(i)
                break
reverse_index.reverse()
print(reverse_index)

for index in reverse_index:
    a = letter[index::-1]
    b = letter[index:]
    letter = letter[index::-1] + letter[index+1:]
print(*letter, sep="")
