## Set interface

---
Set은
1. 저장 순서를 유지하지 않는다.(LinkedHashSet 제외)
2. 중복 값을 허용하지 않는다.

* HashSet : 입력 순서를 보장하지 않고, 중복 값을 허용하지 않는다.
* LinkedHashSet : 순서를 보장하고, 중복 값을 허용하지 않는다.
* TreeSet : 입력 순서를 보장하지 않고, 중복 값을 허용하지 않는다. + 가중치(특정 규칙)에 따른 순서대로 정렬된다.

### Hash가 붙는 이유??
hash에 의해 데이터의 위치를 특정시켜 해당 데이터를 빠르게 색인(search)할 수 있게 만든 것이다.

그렇기 때문에 삽입, 삭제, 색인이 매우 빠른 컬렉션 중 하나다.

## Map interface

---
Map은
1. key 중복 불가, value는 중복가능
2. 순서 보장 불가
3. 정렬 불가(HashMap 제외)

* HashMap : 삽입 순서 보장하지 않고, 정렬 불가능
  * Hash 함수를 이용해 삽입/삭제/조회 연산 O(1)을 보장한다.
* LinkedHashMap : 삽입 순서 보장, 정렬 불가능
  * 삽입/삭제가 느리다.
* TreeMap : 삽입 순서 보장, 정렬 가능
  * 삽입/삭제가 느리다.
* HashTable : 과거에 사용하던 클래스로 더 이상 지원하지 않는 클래스니 사용 지양!