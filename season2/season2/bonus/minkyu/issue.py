a = [1,2,3,4]

if  a[0] == 'X' and a[100] == 1:
    print("????")
else:
    print("WTF")

#############################################

if a[100] == 1 and a[0] == 'X':
    print("????")
else:
    print("WTF")

"""
이건 그냥 몰랐던 사실을 알아서 넣어놨다.
파이썬에서 if 조건1 and 조건2일때
조건1이 False라면 조건2가 무엇이든지간에 바로 else문을 타게된다.
무슨 말이냐면 조건2가 indexerror나 기타 error를 만드는 식이여도 조건1이 틀렸다면 그냥 else문을 타게된다.
파이썬에서는 if 조건1 and 조건2 or 조건3 ···일 때 왼쪽 식부터 훑는 것 같다.
"""