'''
/*문제 정보 */
2121번 - 넷이 놀기
난이도 - 실버 3
/*풀이 방법 */
민규의 조언으로 set으로 받아서 x,y값에 a,b를 더한 값이 있는지 확인해서 카운트를 센다.
'''
n = int(input())

a,b = map(int,input().split())

set1 = set()
for i in range(n):
    x,y = map(int,input().split())
    set1.add((x,y))

list1 = list(set1)
count = 0
for i in range(n):
    x,y = list1[i]
    if (x+a,y) in set1 and (x,y+b) in set1 and (x+a, y+b) in set1:
        count +=1

print(count)
'''
/*오답 노트*/
/*느낀 점*/
이건 또 왜 시간초과야..... 애들아 도와줭....
'''