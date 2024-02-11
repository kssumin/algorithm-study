
def multiple(A,B,C):
    if B==1:
        return A
    else:
        x = multiple(A,B//2,C)
        if B%2==0:
            return x*x%C
        else:
            return x*x*A%C


# 분할 정복을 이용한 거듭제곱

A,B,C = map(int,input().split())

print(multiple(A,B,C))
