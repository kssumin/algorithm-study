# 해시 알고리즘

데이터를 빠르게 넣거나 뺄 때 사용한다.   
파이썬에서는 set와 dict(딕셔너리)가 해시 테이블로 되어있다.

## 해시 테이블
- 키 : 값 (key : value)쌍으로 이루어진 데이터 구조를 말한다. key값으로 value를 찾는다.

장점 : 데이터의 저장과 검색이 빠르다.(list에서 검색 할 때 O(n), 해시 테이블에서 검색 할 때 O(1))   
단점 : 일반적으로 저장공간이 더 많이 필요하다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FRf9ew%2FbtqBD2nxuS2%2FNcjU5klHVOqPfEm28syiFk%2Fimg.png">
위 사진과 같이 key 값으로 데이터를 입력 받으면 hash function을 거쳐 key가 임의의 값으로 바뀌고 그 값과 value로 해시 테이블에 저장된다.
