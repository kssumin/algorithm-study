# BJ 10816 : 숫자 카드 2 / SILVER IV / 860ms

import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().strip().split(' ')))

m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().strip().split(' ')))

n_cnt = dict()

for i in n_list:
    if i in n_cnt:
        n_cnt[i] += 1
    else:
        n_cnt[i] = 1

for num in m_list:
    if num in n_cnt:
        print(n_cnt[num], end=' ')
    else:
        print(0, end=' ')



'''
NOTE:
시도 1) 리스트만 사용해서 for문과 if문으로 코드를 짰다.

for i in range(m):
    if m_list[i] in n_list:
        cnt[i] = n_list.count(m_list[i])
print(' '.join(list(map(str, cnt))))

문제점 : 시간 초과

------------------------------------------------------
시도 2) 딕셔너리(해시)를 사용했다.

# n_list를 오름차순 정렬 후 중복 제거 -> 리스트로 형태 변경
n_list_ss = list(set(sorted(n_list)))

# n_cnt의 key : 'n_list_ss의 원소'로 설정
# n_cnt의 value : '해당 key값이 n_list 내에 존재하는 개수'로 설정
for i in range(len(n_list_ss)):
    n_cnt[n_list_ss[i]] = n_list.count(n_list_ss[i])

문제점 : 시간 초과
내가 짠 코드는 for문 반복에서 시간복잡도 O(n), 매 반복마다 실행되는 count의 시간복잡도가 O(n)이기 때문에 전체 시간복잡도는 O(n^2)이 된다.
리스트를 정렬할 필요도 없다고 한다. set() 사용하면 자동 오름차순 정렬된다. sorted()로 최대 50만 개의 원소를 정렬하는 데에도 O(nlogn)의 시간복잡도가 소요된다.
O(n^2) > O(nlogn) 이므로 최종 시간복잡도는 O(n^2)

------------------------------------------------------
시도 3) 검색해보고 다른 접근법으로 딕셔너리를 사용했다.

for i in n_list:
    if i in n_cnt:
        n_cnt[i] += 1
    else:
        n_cnt[i] = 1

n_list에 있는 원소들이 n_cnt 딕셔너리에 있는지 없는지만 판단하고 덧셈 연산만 시행하면 돼서 시간 복잡도가 O(n)이다.

------------------------------------------------------
느낀 점) 시간 복잡도를 계산해보는 연습을 해야겠다.

'''
