def divide(N, start_x, end_x, start_y, end_y):

    if N==0:
        return
    
    # 현재 종이가 모두 같은 숫자로 이루어지지 않았을 경우
    if(not determine(start_x,end_x,start_y,end_y)):
        N = (end_x - start_x)//3

        divide(N,start_x, start_x+N, start_y, start_y+N)

        divide(N,start_x+N, start_x+2*N, start_y, start_y+N)

        divide(N,start_x+2*N, end_x, start_y, start_y+N)

        divide(N,start_x, start_x+N, start_y+N, start_y+2*N)

        divide(N,start_x+N, start_x+2*N, start_y+N, start_y+2*N)

        divide(N,start_x+2*N, end_x, start_y+N, start_y+2*N)

        divide(N,start_x, start_x+N, start_y+2*N, end_y)
        
        divide(N,start_x+N, start_x+2*N, start_y+2*N, end_y)

        divide(N,start_x+2*N, end_x, start_y+2*N, end_y)


def determine(start_x, end_x, start_y, end_y):

    answer = arr[start_y][start_x]
    # print("---------------")
    # print(answer)
    # print(f"start_x : {start_x}, end_x : {end_x}, start_y : {start_y}, end_y : {end_y}")

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if arr[y][x]!=answer:
                # print(False)
                return False

    

    # for y in range(start_y,end_y):
    #     for x in range(start_x,end_x):
    #         print(arr[y][x],end="")
    #     print()

    cnt[answer] += 1
    
    # print(True)
    return True


N = int(input())

arr = []
cnt = {
    0 : 0,
    1 : 0,
    -1 : 0
}

for i in range(N):
    arr.append(list(map(int, input().split())))

divide(N,0,N,0,N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])