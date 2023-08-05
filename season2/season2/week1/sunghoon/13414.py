'''
/*문제 정보 */
13414번 - 수강신청
난이도 - 실버 3
/*풀이 방법 */
이게 새로고침을 하면 순서가 뒤로 밀리는거 생각했을 때 set은 순서가 뒤죽박죽 되니까 안쓰고
for문으로 돌려서 조건에 맞게 순서 맞추고 정원에 맞게 출력 해줬다.
'''
k,l = map(int, input().split())
list1 = []
for i in range(l):
    a = int(input())
    list1.append(a)

list2 = []
for i in list1:
    if i in list2:
        list2.remove(i)
    if i not in list2:
        list2.append(i)

for i in range(k):
    print(list2[i])
'''
/*오답 노트*/
/*느낀 점*/
아 시간초과 떠용 너무 간단하게 생각했나... 그리고 이상하게 프린트 되어요ㅠㅠ

'''