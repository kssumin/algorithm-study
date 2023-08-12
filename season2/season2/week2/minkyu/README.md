# 스택, 큐
## 스택    
데이터가 들어온 순서대로 데이터가 쌓이고, 데이터를 삭제할 때 가장 나중에 들어온 데이터가 가장 먼저 삭제되는 자료구조이다. - 후입 선출
스택 내부의 데이터는 Top으로 정한 곳에서만 접근이 가능하다.
- 스택의 활용
  - 재귀 알고리즘
  - 함수의 호출 순서
  - 인터넷 브라우저 방문 순서
## 큐
가장 먼저 들어온 데이터가 가장 먼저 삭제되는 자료구조이다. - 선입 선출
- 큐의 활용
  - 프린터 출력
  - 홈페이지 대기열  
# 얕은 복사와 깊은 복사    
얕은 복사와 깊은 복사를 알아보기 전에 일단 mutable 객체와 immutable 객체의 차이를 알아야 한다.
|class|설명|구분|
|------|---|---|
|list |mutable 한 순서가 있는 객체 집합|mutable|
|set  |mutable 한 순서가 없는 고유한 객체 집합|mutable|
|dict |key와 value가 맵핑된 객체, 순서 없음|mutable|
|bool |참,거짓	|immutable|
|int  |정수	|immutable|
|float|실수	|immutable|
|tuple|immutable 한 순서가 있는 객체 집합	|immutable|
|str  |문자열|immutable|

객체 a를 어떤 변수 b에 할당하면 변수 b에 a의 메모리 주소를 할당한다.
얕은 복사의 예시를 보자.
```python
a = ['a', 'b', 'c']
b = a
b[0] = 'x'
```
a 에 mutable한 객체의 메모리 주소를 할당해주었고, b에도 그 객체의 메모리 주소를 똑같이 할당했다.
보통 위처럼 코드를 작성하면 a의 값들은 유지하고 b만 바꾸고 싶은 경우일텐데, 출력은 아래와 같이 된다.
```
a =  ['x', 'b', 'c']
b =  ['x', 'b', 'c']
```
b 변수에 a 값들을 복사해주고 싶었는데, 메모리 주소를 할당해서 a와 b가 가리키는 주소가 같아진 것이다.
따라서 a와 b는 같은 객체X이므로, b[0] 값을 바꿔주어도 X[0]의 값을 바꾼 것일뿐이다.
```python
a = []
print(id(a))
a.append(1)
print(id(a))
a[0] = 2
print(id(a))
```
또, 어떤 변수에 mutable한 객체가 할당되면 안의 값이 변경되더라도 재할당되기전까지는 그때의 메모리 주소는 계속 유지된다.    
직접 출력해보면 같은 값이 출력된다는 것을 알 수 있다.    
하지만 어떤 변수에 immutable한 객체가 할당되면 안의 값을 변경할 수 없으니 재할당하는 수밖에 없어서 메모리 주소가 달라진다.
따라서 얕은 복사는 mutable한 객체를 할당할 때 일어나는 문제이다.

커밋 제목을 잘못 작성해서 다시 작성합니당