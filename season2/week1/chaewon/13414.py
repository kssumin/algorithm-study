# BJ 13414 : 수강신청 / SILVER III / 300ms

import sys

# 수강 가능 인원 k명, 수강신청 버튼을 클릭한 사람 length명
k, length = map(int, sys.stdin.readline().strip().split(' '))

# 수강신청 버튼을 클릭한 사람의 학번 리스트
student_ids = list(sys.stdin.readline().strip() for _ in range(length))

# 규칙1에 따른 중복 제거 : 수강신청 버튼을 한 번 더 클릭한 사람은 뒤로 밀려남
# 즉, student_ids에 중복 존재하는 학번은 인덱스가 가장 큰 학번만 남김
student_ids.reverse()
student_ids = list(dict.fromkeys(student_ids))              # # dict.fromkeys(keys, values) : dictionary 생성 메소드
student_ids.reverse()

result = student_ids[:k]

print('\n'.join(result))
