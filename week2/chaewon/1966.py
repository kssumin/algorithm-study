# BJ 1966 : 프린터 큐 / SILVER III / 68ms

import sys
from collections import deque

# 테스트 케이스의 수
t = int(sys.stdin.readline().strip())

for _ in range(t):
    # n : 전체 문서의 개수, m : 몇 번째로 인쇄되었는지 궁금한 문서의 index
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    # 문서의 중요도 큐
    doc_weights = deque(map(int, sys.stdin.readline().strip().split(' ')))

    cnt = 0

    # 큐가 비어있지 않는다면 계속 검사 실시
    while doc_weights:

        # 큐 내 값들의 max값을 저장
        max_weight = max(doc_weights)

        # 큐에서 나오는 값을 변수로 저장
        front_weight = doc_weights.popleft()

        # 큐에서 값을 빼내면, 내가 찾고자 하는 문서의 index가 하나씩 감소함
        m -= 1

        # 큐의 max값과 큐에서 나온 값이 같다면
        if max_weight == front_weight:

            # 1) cnt + 1을 수행
            cnt += 1

            # 2) m이 음수인지 확인
            #    m이 음수라면, 내가 찾고자 했던 문서의 index가 0이라는 뜻, 즉 front_weight = 내가 찾고자 한 문서
            #    그러므로 cnt 출력 후 while문 탈출
            if m < 0:
                print(cnt)
                break

        # 큐의 max값과 큐에서 나온 값이 다르다면
        else:

            # 1) 큐에서 나온 값을, 큐의 맨 뒤에 삽입 = 큐에서 나온 값의 중요도가 최대가 아니다 = 아직 인쇄될 순서가 아니다
            doc_weights.append(front_weight)

            # 2) m이 음수인지 확인
            #    m이 음수라면, 내가 찾고자 했던 문서의 index가 0이라는 뜻, 이 경우에는 해당 값이 큐의 맨 뒤로 삽입되므로
            #    m을 큐의 마지막 index로 설정해줌
            if m < 0:
                m = len(doc_weights) - 1


'''
NOTE:

뭔가 큐를 쓰는 게 맞는 것 같긴 한데, 도저히 감을 못잡겠어서 리스트로 풀이를 시도하다가 결국 답을 찾아봤다.

------------------------------------------
리스트로 풀이할 때, 
찾고자 하는 값이 최대일 경우는 쉽게 정답을 출력할 수 있었고,
찾고자 하는 값이 최대가 아닌 경우에도 해당 값을 리스트 맨 뒤에 삽입하는 방식으로 값을 쉽게 얻을 수 있었다.

index로 접근해서, list[list.index(list[m])]을 사용하면 위 두 조건은 출력 가능한데,
리스트 내에 중복값이 있을 경우에는 정답을 출력하지 못했다ㅠㅠ
찾고자 하는 값이 중복값에 해당할 경우, index로 접근하면 가장 처음 나온 중복값의 index를 출력하기 때문이다.

ex) list = [1, 1, 9, 1, 1, 1] 이고, 0번째 문서가 몇 번째로 출력되는지 알고 싶다고 했을 때,
    list_sorted = [9, 1, 1, 1, 1, 1] 처럼, list 앞에 있던 두 개의 1이 list 뒤로 삽입되면서
    정답은 5가 되는데, 출력값은 2로 출력됐다....
    
------------------------------------------
구글링 해본 결과
핵심 아이디어는, 나의 숫자(m번째 인덱스에 해당하는 숫자)가 남은 큐 중에서 가장 큰 수가 될 때까지 검사를 실시한다는 것!!

내가 리스트 내 값을 리스트 맨 뒤로 삽입할 때, m의 인덱스 변화까지 팔로업했다면 리스트로도 해결이 가능했을 것 같다.
자세한 것은 라인 별 주석을 참고바란다!!

'''