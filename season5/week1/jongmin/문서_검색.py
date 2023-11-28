# while 반복 횟수 * word.find() 때문에 시간 복잡도가 n**2 이 된다.
# 더 빠른 방법 필요

word = input().rstrip()
find_word = input().rstrip()
cnt = word.count(find_word)

# 아래는 기존 코드ㅋㅋ
"""
while len(word) >= len(find_word):
  idx = word.find(find_word)
  if idx!=-1:
    word = word[idx+len(find_word):]
    cnt += 1
    #print(word)"""

print(cnt)