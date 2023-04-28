import sys
input = sys.stdin.readline

letter1 = list(input().rstrip())
letter2 = list(input().rstrip())

table = [[0 for _ in range(len(letter2) + 1)] for _ in range(len(letter1) + 1)]

for i in range(len(letter1)):
    for j in range(len(letter2)):
        if letter1[i] == letter2[j]:
            table[i + 1][j + 1] = table[i][j] + 1
        else:
            table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])

print(table[-1][-1])


"""
못 풀겠어서 구글링했다....나는 dp가 너무 어렵다... 
아래 사이트를 참고해서 공부했다.
https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

원리는 알았는데 이걸 나 혼자서는 절대 무슨일이 있어도 못 알아냈을 것 같다.
"""