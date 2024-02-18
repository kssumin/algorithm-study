def heapAdd(N, key):
    heap.append(key) # 끝에 노드 추가
    heapUp(N) # 마지막 노드를 heapUp

def heapUp(k):
    if k>0:
        p = (k-1)//2
        if abs(heap[k]) < abs(heap[p]): # 절댓값 힙이므로, 부모보다 작으면 heapUp
            heap[k],heap[p] = heap[p],heap[k]
            heapUp(p)
        elif abs(heap[k])==abs(heap[p]):
            if heap[k] < heap[p]: # 부모와 절댓값이 같을 때, 현재 값이 작다면 swap
                heap[k],heap[p] = heap[p],heap[k]
                heapUp(p)

def heapDelete(N):
    root = heap[0]
    heap[0] = heap[-1]
    heap.pop(-1)
    N -= 1
    heapDown(0,N)
    return root

def heapDown(k,N):
    if k <= (N-2)//2: # 비단말일 경우, 배열의 시작이 0번 인덱스부터 시작일 경우, 비단말 노드의 범위는 0~(N-2)//2 까지이다.
        l = 2*k + 1
        r = 2*k + 2
        # print(f"l:{l},r:{r},k:{k}")
        m = minIndex(k,l,r,N)
        if m!=k:
            heap[k],heap[m] = heap[m],heap[k]
            heapDown(m,N)

def minIndex(k,l,r,N):
    # 비교할 노드가 3개
    if r<=N-1:
        # 절댓값 세 개가 모두 다른 경우
        if abs(heap[k]) < abs(heap[l]) and abs(heap[k]) < abs(heap[r]):
            return k
        elif abs(heap[l]) < abs(heap[k]) and abs(heap[l]) < abs(heap[r]):
            return l
        elif abs(heap[r]) < abs(heap[l]) and abs(heap[r]) < abs(heap[l]):
            return r

        # 절댓값 세 개 중 두 개가 같을 경우
        elif abs(heap[r]) == abs(heap[l]):
            if abs(heap[l]) > abs(heap[k]):
                return k
            else:
                if heap[r] < heap[l]:
                    return r
                else:
                    return l
        elif abs(heap[r]) == abs(heap[k]):
            if abs(heap[k]) > abs(heap[l]):
                return l
            else:
                if heap[k] < heap[l]:
                    return k
                else:
                    return l
        elif abs(heap[l]) == abs(heap[k]):
            if abs(heap[k]) > abs(heap[r]):
                return r
            else:
                if heap[k] < heap[r]:
                    return k
                else:
                    return r

    # 절댓값 세 개가 모두 같을 경우
        elif abs(heap[r]) == abs(heap[l]) and abs(heap[l]) == abs(heap[k]):
            if heap[r] < heap[l] and heap[r] < heap[k]:
                return r
            elif heap[l] < heap[r] and heap[l] < heap[k]:
                return l
            elif heap[k] < heap[l] and heap[k] < heap[r]:
                return k

    # 비교할 노드가 2개
    else:
        if abs(heap[k]) == abs(heap[l]):
            if heap[k] < heap[l]:
                return k
            else:
                return l
        elif abs(heap[k]) < abs(heap[l]):
            return k

        else:
            if heap[k] < heap[l]:
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
        if len(heap)>0: answer.append(heapDelete(len(heap)))
        else: answer.append(0)

for i in answer:
    print(i)
