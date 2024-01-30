import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    grade_list = []
    for _ in range(N):
        grade_list.append(tuple(map(int, input().split())))
    grade_list.sort()
    result = [grade_list[0]]
    min_grade = result[0][1]
    for j in range(1, len(grade_list)):
        if grade_list[j][1] < min_grade:
            result.append(grade_list[j])
            min_grade = min(min_grade, grade_list[j][1])
    print(len(result))