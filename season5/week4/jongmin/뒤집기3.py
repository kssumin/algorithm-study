from collections import deque

word = input()
LENGTH = len(word)

for i in range(LENGTH-1):
    # i는 문자열의 인덱스
    if word[i] < word[i+1]:
        word = word[:i+1][::-1] + word[i+1:]
        word = word[:i+2][::-1] + word[i+2:]

    # 문자열의 replace 라는 메소드도 있지만, 이 메소드를 사용할 경우
    # ABAB 와 같은 상황이 오면 문자열 안의 일치하는 패턴을 모두 교체하므로 좋지 않다.

print(word[::-1])