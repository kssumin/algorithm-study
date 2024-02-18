# O(logN)
def heapAdd(N,key):
    heap.append(key) # 끝에 노드 추가
    heapUp(N) # 끝에 추가한 노드(인덱스 : N)를 heapUp
    #print(heap)

def heapUp(k):
    if k>0:
        p = (k-1)//2
        if heap[k] <= heap[p]: # 최소 힙이므로, 부모 노드보다 작으면 heapUp
            heap[k],heap[p] = heap[p],heap[k]
            heapUp(p)

# O(logN)
def heapDelete(N): # 맨 마지막 노드를 루트 노드로 복사하고, 마지막 노드를 삭제한다.
    root = heap[0]
    heap[0] = heap[N-1]
    heap.pop(-1)
    N -= 1
    heapDown(0,N)
    #print(heap)
    #print(heap)
    return root

def heapDown(k,N):
    if k <= (N-2)//2: # 비단말일 경우, 배열의 시작이 0번 인덱스부터 시작일 경우, 비단말 노드의 범위는 0~(N-2)//2 까지이다.
        l = 2*k + 1
        r = 2*k + 2

        m = minIndex(k,l,r,N) # 본인과 자식 노드들의 값을 비교해서 최소의 값을 가지는 노드 찾기

        if m!=k: # 본인이 최소가 아니면 최소와 스위치
            heap[k],heap[m] = heap[m],heap[k]
            heapDown(m,N)

def minIndex(k,l,r,N):
    if r<=N-1: # 비교 노드 수가 3개인 경우
        if heap[k] <= heap[l] and heap[k] <= heap[r]:
            return k
        elif heap[l] <= heap[k] and heap[l] <= heap[r]:
            return l
        elif heap[r] <= heap[l] and heap[r] <= heap[l]:
            return r
    else: # 비교 노드 수가 2개인 경우
        if heap[k] <= heap[l]:
            return k
        else:
            return l

N = int(input())
heap = list()
answer = list()

for _ in range(N):
    x = int(input())
    if x!=0: heapAdd(len(heap),x)
    else:
        if heap:
            answer.append(heapDelete(len(heap)))
        else:
            answer.append(0)

for i in answer:
    print(i)