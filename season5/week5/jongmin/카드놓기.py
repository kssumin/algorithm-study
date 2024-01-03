from itertools import permutations

N = int(input())
K = int(input())
cards = []

for _ in range(N):
    cards.append(input())

# python itertools 좋아요
    
p = permutations(cards, K)
numbers = set(["".join(i) for i in p])


print(len(numbers))