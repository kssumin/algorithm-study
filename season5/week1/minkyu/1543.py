import sys
input = sys.stdin.readline

letter = input()
find_letter = input()[:-1]
result = letter.split(find_letter)
print(len(result)-1)
