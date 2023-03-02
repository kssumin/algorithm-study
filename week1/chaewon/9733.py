# BJ 9733 : 꿀벌 / SILVER V / 40ms

import sys

# 여러 줄 입력 받기
lines = sys.stdin.readlines()

work_names = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
work_cnt = dict.fromkeys(work_names, 0)

total_cnt = 0
for line in lines:
    work_list = list(line.split())
    for i in work_list:
        if i in work_names:
            work_cnt[i] = work_cnt.get(i, 0) + 1
        total_cnt += 1


for work in work_names:
    print(work, work_cnt[work], '{:.2f}'.format(work_cnt[work] / total_cnt))


print('Total', total_cnt, '1.00')


'''
NOTE:

1) 줄바꿈
입력 조건이 '공백', '줄바꿈' 두 개인데,
'공백'을 만족하는 코드는 짰는데 '줄바꿈'을 만족하는 건 못짜서 구글링해봤다ㅠㅠ

sys.stdin.readline()은 많이 썼는데
sys.stdin.readlines()는 처음이라서 생소했다.

readlines()를 쓰면 여러 줄의 입력을 받을 수 있고, ctrl+d를 통해 입력을 마칠 수 있다.
예전엔 백준에서 ctrl+d를 안 해줘서 해당 함수를 쓸 수 없었다는 것 같은데 지금은 잘 작동한다!!

------------------------------------------------------
2) dict.fromkeys(seq, value)
이 메소드는 13414 수강신청 문제 풀 때 공부해뒀던 건데 여기서도 써봤다!!
구글링 해서 찾은 코드에서는, 해당 메소드를 사용하지 않고 for문 돌려서 dict[work] = 0 으로 초기화해줬던데
이 메소드 쓰니까 간략화할 수 있어서 좋은 것 같다~~

------------------------------------------------------
3) 출력 조건 '주어진 목록에 없는 일은 출력하지 않는다'
이 조건을 못 봐서 계속 오류가 났다ㅠ
15번줄의 if문만 추가하면 됐던 건데...!! 조건을 잘 읽어야겠다.

------------------------------------------------------
4) dict.get(a, b)
dict에 'a'라는 key가 있으면 해당하는 value를 출력하고,
'a'라는 key가 없으면 b를 반환하는 메소드이다.

처음에는 다음과 같이 코드를 짰다.

for i in work_list:
    if i in work_cnt:
        work_cnt[i] += 1
    else:
        work_cnt[i] = 1

문제점 : 입력 시에 줄이 바뀌면, work_list가 새로 갱신되기 때문에 입력에 존재하던 값도 존재하지 않는 것으로 인지한다.
ex) 입력 : Re Cc Pt
          Cc Cm
          
    12번 for문에 의해,
    첫 번째 반복 : work_list = ['Re', 'Cc', 'Pt']
    두 번째 반복 : work_list = ['Cc', 'Cm']
    첫 번째 반복문에서 'Cc'가 존재함에도 불구하고 두 번째 반복문에서는 'Cc'의 value가 1로 초기화된다.

구글링해서 찾은 코드에서 이 get 메소드를 사용한 것을 보고 이런 식의 활용이 가능하다는 것을 알게 되었다!!
------------------------------------------------------
느낀 점) 몬가... 쉬운 문제인데 놓친 포인트가 많아서 반성 중이다 8_8

'''