# BJ 1541 : 잃어버린 괄호 / SILVER II / 40ms

import sys

sys.stdin = open("input.txt", "rt")

eq = sys.stdin.readline().strip()

first = eq
second = ''

if '-' in eq:
    first = eq[:eq.index('-')]
    second = eq[eq.index('-') + 1:]

# print('first: ', first)
# print('second: ', second)

if '+' in first:
    first = first.replace('+', ' ')

first_list = list(map(int, first.split()))
first_sum = sum(first_list)


if '+' in second or '-' in second:
    second = second.replace('+', ' ')
    second = second.replace('-', ' ')
second_list = list(map(int, second.split()))
second_sum = sum(second_list)

# print('first_sum: ', first_sum)
# print('second_sum: ', second_sum)

print(first_sum - second_sum)