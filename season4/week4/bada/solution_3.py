answer = 0
def DFS(k, cnt, dungeons, check):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if check[i] == 0 and k >= dungeons[i][0]:       # 방문하지 않은 던전이고, 현재 피로도가 해당 던전을 방문하기 위한 최소 피로도보다 크면
            check[i] = 1
            # ** 중요 **
            # 이전 노드로 다시 back할 때, check 값만 0으로 바꿔줄 뿐 아니라 
            # 현재 피로도의 수도 해당 노드를 방문하기 전의 피로도로 다시 복구해줘야 한다. 
            # 따라서, 직접적으로 k 값과 cnt 값을 바꿔주기 보다는, DFS 함수 내에서 보내주는 매개변수의 값을 수정해줘야 한다.
            DFS(k-dungeons[i][1], cnt+1, dungeons, check)
            check[i] = 0
    

def solution(k, dungeons):
    # answer = 0
    global answer
    check = [0]*len(dungeons)       # 방문 여부 체크하는 배열
    
    # cnt: 탐험한 던전 개수, k: 남은 피로도
    DFS(k, 0, dungeons, check)     # 0: 방문한 던전의 개수를 0으로 DFS 함수에 넘겨준다.
    
    return answer