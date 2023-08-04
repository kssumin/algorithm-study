'''
/*문제 정보 */
9733번 - 꿀벌
난이도 - 실버 5
/*풀이 방법 */
처음에 하나하나 카운트를 어떻게 할까 생각했는데 딕셔너리로 풀면 된다는걸
민규 코드보고 알았다. 나머지는 반복문으로 카운트 해주고 key, value 값 받아
서 출력했다.
'''
bee = {"Re":0,"Pt":0,"Cc":0,"Ea":0,"Tb":0,"Cm":0,"Ex":0}
l = input()
result = l.split()

for i in result:
    if i in bee:
        bee[i] +=1

for key, value in bee.items():
    print("{} {} {:.2f}".format(key, value,value/len(result)))

print("Total "+str(len(result))+" 1.00")
'''
/*오답 노트*/
/*느낀 점*/
print(key, value, round(value/len(result), 2))로 할 때, Ex가 0.0만
표기 되는 문제를 format을 사용해 해결... 근데 제출하면 틀렸대용... 뭐가 문젤까
'''