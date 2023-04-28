import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
for i in range(1, n):
    num_list[i] = max(num_list[i], num_list[i - 1] + num_list[i])
print(max(num_list))

"""
dp는 어렵다. 엄청 오래 풀어봤는데 못 풀어서 구글링 했다.
처음 코드를 짤 때 출력해야할 결과값을 num_list에 저장했다.
ex) 10 -4 3 1 5 6일 때
   10 10 10 10 15 21···
그랬더니 변수를 새로 파고, 또 for문으로 -가 있었던 곳을 찾아냈어야했다.

출력해야할 결과값을 dp 리스트에 차례로 갱신했더니 오히려 dp를 못 쓰게 됐다.
dp 문제를 풀 때 메모이제이션은 계산한 값을 저장하기 위한 수단으로 사용하자.
무조건 결과값을 저장해야 되는게 아니라는 걸 알아야겠다...
틀에 박혀서 못 풀었다. ㅠ

풀이
ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
"""