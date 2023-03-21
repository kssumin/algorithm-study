# 힙 자료구조란
 - 완전 이진 트리의 일종이다.
   - 완전이진트리란
    1) 완전 이진트리는 마지막 레벨을 제외 하고 모든 레벨이 완전히 채워져 있어야 한다.
    2) 노드가 왼쪽에서 오른쪽으로 채워져야 한다.

 -  우선순위 큐를 위하여 만들어진 자료구조이다.
 - 여러 개의 값들 중에서 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조이다.
 - 힙은 반정렬 상태를 유지한다.
   - 정렬이 되어 있지만 완벽히 되어 있지 않다. (부모 노드에 있는 값이 자식 노드의 값보다 항상 크다)
# 힙 모듈 메소드    
[참고주소](https://python.flowdas.com/library/heapq.html)
1. heapq.heappush(heap, item)    
힙 불변성을 유지하면서, item 값을 heap으로 푸시한다.
2. heapq.heappop(heap)    
힙 불변성을 유지하면서, heap에서 가장 작은 항목을 팝하고 반환한다. pop하지 않고 접근만 하려면 heap[0]을 사용하면 된다.
3. heapq.heappushpop(heap, item)    
힙에 item을 푸시한 다음, heap에서 가장 작은 항목을 팝하고 반환한다. heappush()한 다음 heappop()을 하는 것이 더 효율적으로 작용한다.
4. heapq.heapreplace(heap, item)    
heap에서 가장 작은 항목을 팝하고 반환하며, 새로운 item도 푸시한다.
 - 4번과 5번이 같아 보이지만 3번은 push 후 pop, 4번은 pop 후 push 이므로 3번은 item이 반환될 가능성이 있지만 4번은 그렇지 않다.
5. heapq.heapify(x)    
리스트 x를 힙으로 변환한다.
6. heapq.merge(*iterables, key=None, reverse=False)    
여러 정렬된 입력값을 합쳐서 이터러블 객체로 반환한다. (ex) list(heapq.merge([1,5,6,8],[2,3,4,9]))) == [1,2,3,4,5,6,8,9]
 - Iterator 객체란? : Iterator의 __next__() 나 내장 함수인 next()를 부르면서, 원소(element)를 순차적으로 반환 할 수 있는 객체    
 [참고주소](https://emjayahn.github.io/2019/07/15/iterator-generator/)
7. heapq.nlargest(n, iterable, key=None)    
n개의 가장 큰 요소로 구성된 리스트를 반환한다.
8. heapq.nsmallest(n, iterable, key=None)    
n개의 가장 작은 요소로 구성된 리스트를 반환한다..
