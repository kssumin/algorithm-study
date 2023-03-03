<h2>1주차 이론 정리</h2>
- - -
https://www.notion.so/cheezeasy/Week-2-78f8bcef6102446380f43275f187fd17?pvs=4#3305434e8eb6490db3cbcda55d5b3c83
- - -

<h3>데이터 타입(list, tuple, dict, set) 차이점 정리</h3>

1. List : 순서 존재, Indexing 존재, mutable(변경 가능)
    - list는 index를 통해 값을 변경할 수 있다.


2. Tuple : 순서 존재, Indexing 존재, immutable(변경 불가)
    - tuple은 index가 존재하긴 하지만, 값을 변경할 수는 없다.
    - 값을 변경하려면 list(tuple) → 변경 → tuple(list) 의 과정을 거쳐야 한다.

    - unpacking : tuple의 값을 차례대로 변수에 대입 - tuple을 사용하는 이유
    - ex) a = 2, b = 3일 때, a와 b의 값을 교환하세요
        - tuple X : temp = b, b = a, a = temp
        - tuple O : a, b = b, a **(간편)**

3. Dictionary : key-value, 중복 불가, 순서 없음
    - dict in : dictionary의 크기와 관계 없이 항상 시간 복잡도가 O(1)이다. <<< list in : 시간 복잡도 O(n)

4. Set : key, 중복 불가, 순서 없음
    - 집합의 개념으로, union, intersection, difference, issubset 등의 메소드가 있다.
