# A*알고리즘

## 다익스트라를 풀다보니 너무 느렸다

다익스트라를 풀다보니 너무 느려서 다른 좋은 알고리즘이 있는지 찾아보던 도중 A*알고리즘이 있다는 것을 알게 되었다.

## 그러면 원리는 어떻게 되는 가?

가장 기본이 되는 원리는 다음과 같다.

f(x) = g(x) + h(x)

> F - 현재까지 이동하는데 걸린 비용과 예상 비용을 합친 총 비용  
  G - 시작점 A로부터 현재 사각형까지의 경로를 따라 이동하는데 소요되는 비용  
  H - 현재 사각형에서 목적지 B까지의 예상 이동 비용.

1. f(x)를 오름차순 우선순위 큐에 노드로 삽입한다.
2. 우선순위 큐에서 최우선 노드를 pop한다.
3. 해당 노드에서 이동할 수 있는 노드를 찾는다.
4. 그 노드들의 f(x)를 구한다.
5. 그 노드들을 우선순위 큐에 삽입한다.
6. 목표 노드에 도달할 때까지 반복한다.

위의 식을 python으로 대충 풀자면 다음과 같다.

```py
/* A* 특징
1. openList와 closeList라는 보조 데이터를 사용한다.
2. F = G + H 를 매번 노드를 생성할 때마다 계산한다.
3. openList에는 현재 노드에서 갈 수 있는 노드를 전부 추가해서 F,G,H를 계산한다.
    openList에 중복된 노드가 있다면, F값이 제일 작은 노드로 바꾼다.
    
4. closeList에는 openList에서 F값이 가장 작은 노드를 추가시킨다.
*/

openList.add(startNode)  # openList는 시작 노드로 init

while openList is not empty:
    # 현재 노드 = openList에서 F 값 가장 작은 것
    currentNode <- node in openList having the lowest F value
    openList.remove(currentNode)  # openList에서 현재 노드 제거
    closeList.add(currentNode)  # closeList에 현재 노드 추가
    
    if goalNode is currentNode:
        currentNode.parent.position 계속 추가 후
        경로 출력 후 종료
        
    children <- currentNode와 인접한 모든 노드 추가
    
    for each child in children:
        if child in closeList:
            continue
        
        child.g = currentNode.g + child와 currentNode 거리(1)
        child.h = child와 목적지까지의 거리
        child.f = child.g + child.h
        
        # child가 openList에 있고, child의 g 값이 openList에 중복된 노드 g값과 같으면
        # 다른 자식 불러오기
        if child in openList and child.g > openNode.g in openList:
            continue
            
        openList.add(child)
```

## 링크

[최단 경로 탑색 - A*알고리즘](http://www.gisdeveloper.co.kr/?p=3897)
[A*알고리즘 정의 및 개념](https://itmining.tistory.com/66)
[파이썬A* 최단 경롤 찾기 알고리즘](https://choiseokwon.tistory.com/210)
