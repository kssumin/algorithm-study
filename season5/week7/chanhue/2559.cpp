//#include <iostream>
//#include <stdio.h>
//
//using namespace std;
//
//int main() {
//	int N, K;
//	int arr[100001] = {0,};
//	int max;
//	scanf("%d %d", &N, &K);
//	for (int i = 1; i <= N; i++) {
//		scanf("%d", &arr[i]);
//		arr[i] = arr[i - 1] + arr[i];
//	}
//	max = arr[K];
//	for (int i = 1; i < N - K + 1; i++) {
//		if (max < arr[i + K] - arr[i]) {
//			max = arr[i + K] - arr[i];
//		}
//	}
//	printf("%d", max);
//	
//}