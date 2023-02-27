# BJ 10816 : 숫자 카드 2 / SILVER IV /

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
처음엔 리스트만 사용해서 for문과 if문으로 아래와 같은 코드를 짰다.
for i in range(m):
    if m_list[i] in n_list:
        cnt[i] = n_list.count(m_list[i])
print(' '.join(list(map(str, cnt))))

그랬더니 시간 초과가 떠서, 딕셔너리(해쉬)로 풀이를 시도했다.


# n_list를 오름차순 정렬 후 중복 제거 -> 리스트로 형태 변경
n_list_ss = list(set(sorted(n_list)))

# n_cnt의 key : 'n_list_ss의 원소'로 설정
# n_cnt의 value : '해당 key값이 n_list 내에 존재하는 개수'로 설정
for i in range(len(n_list_ss)):
    n_cnt[n_list_ss[i]] = n_list.count(n_list_ss[i])

그럼에도 계속 시간 초과가 떠서 결국 검색해봤더니, 위 코드를 13~17번 라인으로 수정해야 했다.

for i in n_list:
    if i in n_cnt:
        n_cnt[i] += 1
    else:
        n_cnt[i] = 1

내가 짠 코드는 for문 반복에서 시간복잡도 O(n), 매 반복마다 실행되는 count의 시간복잡도가 O(n)이기 때문에 전체 시간복잡도는 O(n^2)이 된다.
아래 코드를 보면 n_list에 있는 원소들이 n_cnt 딕셔너리에 있는지 없는지만 판단하면 돼서 시간 복잡도가 O(n)이다.

시간복잡도를 계산해보는 습관을 들여야겠다
'''
