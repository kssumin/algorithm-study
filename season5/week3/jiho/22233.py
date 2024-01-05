import sys

memo, blog = map(int, sys.stdin.readline().split())
word_set = {}
cnt = 0

for i in range(memo):
    word_set[sys.stdin.readline().rstrip()] = 1
    cnt += 1

for j in range(blog):
    using = list(sys.stdin.readline().rstrip().split(','))
    for k in using:
        if k in word_set.keys():
            if word_set[k] == 1:
                word_set[k] = 0
                cnt -= 1
    print(cnt)

