s = input()
str_set = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        str_set.add(s[i:j+1])

print(len(str_set))
