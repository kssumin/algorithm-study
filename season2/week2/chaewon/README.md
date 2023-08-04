# 스택과 큐

https://cheezeasy.notion.site/Week-2-78f8bcef6102446380f43275f187fd17

## 원형 큐
- 큐의 일종
- 원형으로 이루어져 있어, 포화와 불포화 상태를 구분하기 위해서 원하는 큐의 크기보다 +1한 크기로 큐를 선언해야 함
- 원형 큐의 포화 조건
    - (rear + 1) % arraysize == front
    ![queue](C:/Users/user/Downloads/Untitled (1).png)

