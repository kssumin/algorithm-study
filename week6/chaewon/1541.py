# BJ 1541 : 잃어버린 괄호 / SILVER II /

import sys

eq = sys.stdin.readline().strip()
eq_list = []

for i in range(len(list(eq))):
   if type(eq[i]) == str:
        num = eq[:i]
        eq_list.append(num)
        eq_list.append(eq[i])
        eq = eq[i + 1:]

print(eq_list)