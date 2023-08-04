# 원형 큐(Circular Queue)


## 배열을 사용한 Queue의 단점
선형 큐에서 삽입 및 삭제를 반복하면, rear가 맨 마지막 인덱스를 가리키고,
앞에는 비어 있을 수 있지만 이를 꽉 찼다고 인식
앞에 남아있는 (삽입 중간에 Dequeue 되어 비어있는) 공간을 활용할 수 없음


## 원형 큐란?
배열로 구현 된 선형 큐(Linear Queue)의 경우 데이터의 삽입/삭제시 데이터들을 앞/뒤로 당겨주는
과정이 필요해 최악의 경우 O(n)의 시간복잡도를 가지게 됨. 이 단점을 극복한 구조가 원형 큐



### 0. 멤버 변수 & 초기화
<pre><code>
class CircleQueue:

    rear = 0
    front = 0
    MAX_SIZE = 100
    queue = list()
    
    def __init__(self):
    	self.rear = 0
        self.front = 0
        self.queue = [0 for i in range(self.MAXSIZE)]
</code></pre>


### 1. 공백 상태
원형큐가 비워져 있는 경우 __front == rear__ 임.
<pre><code>
def is_empty(self):
	if self.rear == self.front:
    	return True
    return False
</code></pre>


### 2. 포화 상태
공백 상태를 front == rear로 구분했기 때문에 포화 상태는 한칸이 비어있음.
따라서, __포화상태는 배열에 한칸을 비움으로써__ 구분.
<pre><code>
def is_full(self):
	if (self.rear+1)%self.MAX_SIZE == self.front:
    	return True
    return False
</code></pre>


### 3. 데이터 삽입
rear에서 삽입이 이루어지므로, front 값의 변경은 없고, rear += 1을 해줌.
<pre><code>
def enqueue(self, x):
	if is_full():
    	print("ERROR: FULL")
        return
    self.rear = (self.rear+1)%(self.MAX_SIZE)
    self.queue[self.rear] = x
</code></pre>


### 4. 데이터 삭제
front에서 삭제가 이루어지므로, rear 값의 변경은 없고, front += 1을 해줌.
<pre><code>
def dequeue(self):
	if is_empty():
    	print("ERROR: EMPTY")
        return
    self.front = (self.front +1) % MAX_SIZE
    return self.queue[self.front]
</code></pre>

출처 : <https://codingsmu.tistory.com/123>
