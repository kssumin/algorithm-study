N = list(map(int,list(input().rstrip())))
N.sort(reverse=True)

if sum(N)%3==0 and N[-1]==0:
    print("".join(list(map(str,N))))
    
else:
    print(-1)