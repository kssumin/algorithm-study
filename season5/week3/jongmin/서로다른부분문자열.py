s = input().strip()
set_ = set()

# 1부터 n까지...
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        try:
            if s[i:j] not in set_:
                set_.add(s[i:j])
        except:
            pass

# set_을 출력해보면 예제 출력과 동일한데
# len(set_)은 왜 11이 출력되는지 모르겠다..
print(len(set_))

"""
s = input()
set = set()
for i in range(len(s)):
  for j in range(i+1,len(s)+1):
    set.add(s[i:j])
print(len(set))
"""
