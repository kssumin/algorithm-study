import sys; input = sys.stdin.readline

A, B, C = map(int, input().split())
def fpow(A, B):
	if B == 1:
		return A % C
	else:
		x = fpow(A, B//2)
		if B % 2 == 0:
			return (x * x) % C
		else:
			return (x * x * A) % C


print(fpow(A, B))
