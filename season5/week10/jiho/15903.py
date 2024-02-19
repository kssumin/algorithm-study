import sys; input = sys.stdin.readline

cnt1, cnt2 = map(int, input().split())
card_lst = []
card_lst += map(int, input().split())

for _ in range(cnt2):
    card_lst.sort()
    card_lst[0] = card_lst[1] = card_lst[0] + card_lst[1]

print(sum(card_lst))