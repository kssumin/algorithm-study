# 1. 글자 자체가 팰린드롬
# 2. 일부 대칭
# 3. 완전 대칭 

def isPalindrome(s):
  if s == s[::-1]:
    return True
  return False

def toPalindrome(s):
    for i in range(1,len(s)):
      t = s+(s[:i])[::-1]
      #print(t)
      if isPalindrome(t):
        return len(t)


s = input().rstrip()

print(toPalindrome(s))