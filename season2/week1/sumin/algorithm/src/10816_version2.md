나는 key값이 배열에 있는지 loop를 돌면서 확인했다.

### 순차적 탐색

---

* 배열에서 특정 원소를 찾기 위해 index 0부터 순차적으로 탐색한다.
* 따라서 최악의 경우 원하는 값을 찾기 위해 배열의 끝까지 탐색을 해야하기에 시간 복잡도는 O(n)이다.



### 이분 탐색

---

1. 정렬된 배열 안에서 특정 원소를 찾을 때 index left, index right 의 중간값과 특정값을 비교한다.

2. 특정 원소와 중간값을 비교한다.

   * 특정 원소와 중간값이 같으면 탐색을 종료한다.

   * 중간값 < 특정원소 : left = mid + 1로 하여 2를 다시 반복한다.
   * 중간값 > 특정원소 : right = mid -1로 하여 2를 다시 반복한다.

3. left > right 가 된다면 해당 배열에 찾는 원소가 없는 것이다.

범위를 새로 정할 때마다 탐색 범위는 1/2씩 줄어든다. 따라서 시간 복잡도는 O(log n)이다.

![IMG_E88C856A9604-1](https://user-images.githubusercontent.com/88534959/222423081-d1202ec9-aaef-4a38-b41e-6281f03eff34.jpeg)

![IMG_299A6B929F60-1](https://user-images.githubusercontent.com/88534959/222426291-ced61a69-4e8a-4428-a0db-d6b959c243d1.jpeg)



### 해당 문제에서는 이분 탐색을 어떻게 사용할까?

----

이분탐색은 배열을 정렬해서 해당 배열에서 찾고자하는 값이 있는지 없는지 확인한다.

하지만 이 문제를 풀기 위해서는 해당 배열에서 찾고자하는 값이 **몇 개** 있는지 확인해야 한다.

즉, 찾고자 하는 숫자가 시작하는 지점, 끝나는 지점을 찾아야 한다.



### 찾고자 하는 값이 몇 개 존재하는가?

---

* lower bound : 찾고자 하는 숫자 이상의 값이 처음 존재하는 지점
* upper bound : 찾고자 하는 숫자 초과의 값이 처음 존재하는 지점

lower bound, upper bound를 찾아서 upper bound - lower bound를 하면 찾고자 하는 값이 몇 개 존재하는지 알 수 있다.

예제1)

![IMG_FA72C25A9A70-1](https://user-images.githubusercontent.com/88534959/222429686-de1ae98a-2d18-49af-bec9-419b51992970.jpeg)

따라서 찾고자 하는 값은 총 3개이다.



예제2)

![IMG_71AC0FA8E6B3-1](https://user-images.githubusercontent.com/88534959/222429527-08276d27-75f3-48af-9fe5-54ba86c4ea5f.jpeg)



따라서 찾고자 하는 값은 총 0개이다.



처음에는 lower bound -> 찾고자 하는 값이 처음으로 나타난 위치여야 하는 게 아닌가? 라는 생각을 했다. 왜 **이상**이라는 존재가 붙었을까 라는 것에 의문이 들었다.



예제 2번 문제를 풀고나니 이해가 된다.

만약, 이상이라는 존재가 붙지 않았더라면(key와 일치하는 값이 처음으로 나타난 위치), key = 5는 lower bound를 정할 수 없었을 것이다.



### 변형된 이진탐색 코드

---



```java
private static int lowerBound(int[] arr, int key) {
	int lo = 0; 
	int hi = arr.length; 
 
	// lo가 hi랑 같아질 때 까지 반복
	while (lo < hi) {
 
		int mid = (lo + hi) / 2; // 중간위치를 구한다.
 
		/*
		 *  key 값이 중간 위치의 값보다 작거나 같을 경우
		 *  (중복 원소에 대해 왼쪽으로 탐색하도록 상계를 내린다.)
		 */
		if (key <= arr[mid]) {
			hi = mid;
		}
 
		else {
			lo = mid + 1;
		}
 
	}
	return lo;
}
 
private static int upperBound(int[] arr, int key) {
	int lo = 0; 
	int hi = arr.length; 
 
	// lo가 hi랑 같아질 때 까지 반복
	while (lo < hi) {
 
		int mid = (lo + hi) / 2; // 중간위치를 구한다.
 
		// key값이 중간 위치의 값보다 작을 경우
		if (key < arr[mid]) {
			hi = mid;
		}
		// 중복원소의 경우 else에서 처리된다.
		else {
			lo = mid + 1;
		}
	}
	return hi;
}
```

