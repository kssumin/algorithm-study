import sys

# 0,0에서부터 한 변의 길이가 1 ~ N또는M 인 정사각형을 찾는다.
# 그 중에서 네 꼭지점의 값이 같은 사각형을 찾는다.

def find_square(rec,x,y):
  length = min(x,y)
  find_rec = 1
  for i in range(x*y):
    row = i//y
    col = i%y
    for j in range(length):
      # j+1 는 변의 길이
      # 새로 찾은 변의 길이가 마지막으로 찾은 변의 길이보다 크면 진행
      if find_rec < j+1:
        try:
          if rec[row][col] == rec[row+j][col] == rec[row][col+j] == rec[row+j][col+j]:
              find_rec = j+1
              #print(f"find_rec = {find_rec}")
        except:
          pass
    
  return find_rec**2

N,M = map(int, sys.stdin.readline().rstrip().split())

rec = []

for _ in range(N):
  rec.append(list(sys.stdin.readline().rstrip()))

print(find_square(rec,N,M))