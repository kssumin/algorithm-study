# - [20529번](https://www.acmicpc.net/problem/20529) 가장 가까운 세 사람의 심리적 거리 (실버1)
import sys

input = sys.stdin.readline
T = int(input())

mbtis = ["INFP", "INFJ", "INTJ", "INTP", "ISFP", "ISFJ", "ISTJ", "ISTP", "ENFP", "ENFJ", "ENTJ", "ENTP", "ESFP", "ESFJ", "ESTJ", "ESTP"]

def gap(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

mbti_dist = []
for i in range(len(mbtis)):
    mbti_dist.append([])
    for j in range(len(mbtis)):
        mbti_dist[i].append(gap(mbtis[i], mbtis[j]))

def calc_dist(paths):
    a, b, c = paths
    return mbti_dist[a][b] + mbti_dist[b][c] + mbti_dist[c][a]

min_dist = 8
def dfs(mbti_inputs, index, paths):
    global min_dist
    if len(paths) == 3:
        min_dist = min(min_dist, calc_dist(paths))
        return 
    for i in range(index, len(mbti_inputs)):
        dfs(mbti_inputs, i+1, paths+[mbtis.index(mbti_inputs[i])])

for _ in range(T):
    N = int(input())
    mbti_inputs = input().split()
    if N >= 33:
        print(0)
        continue
    dfs(mbti_inputs, 0, [])
    print(min_dist)
    min_dist = 8

