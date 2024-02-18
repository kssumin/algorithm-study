# Bottom-up 방식 힙 구성
def heapCompose(n):
    # 비단말부터 1까지 이동
    for k in range((n-2)//2,-1,-1):
        heapDown(k,n)
        #print(heap)

def heapDown(k,n):
    if k <= (n-2)//2: # 비단말일 경우
        l = 2*k + 1
        r = 2*k + 2
        #print(k,l,r)
        m = minIndex(k,l,r,n)

        if(m!=k):
            heap[m],heap[k] = heap[k],heap[m]
            heapDown(m,n)

def minIndex(k,l,r,n):
    if r <= n-1: # 비교 노드 수가 3개인 경우
        if heap[k] <= heap[l] and heap[k] <= heap[r]:
            return k
        elif heap[l] <= heap[k] and heap[l] <= heap[r]:
            return l
        elif heap[r] <= heap[k] and heap[r] <= heap[l]:
            return r
        
    else: # 비교 노드 수가 2개인 경우
        if heap[k] <= heap[l]:
            return k
        else:
            return l

n,m = map(int, input().split())
heap = list(map(int, input().split()))
heapCompose(n)

for i in range(m):
    s = heap.pop(0) + heap.pop(0)
    heap.append(s)
    heap.append(s)
    #print(heap)
    heapCompose(n)

print(sum(heap))