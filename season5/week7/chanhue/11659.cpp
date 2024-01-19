//#include <iostream>
//#include <vector>
//#include <stdio.h>
//
//using namespace std;
//
//
//int main() {
//	int N, M, i, j;
//	int arr[100001] = { 0, };
//
//	scanf("%d %d", &N, &M);
//	for (int k = 1; k <= N; k++) {
//		scanf("%d",&arr[k]);
//		arr[k] += arr[k - 1];
//	}
//	for (int k=0; k < M; k++) {
//		scanf("%d %d", &i, &j);
//		printf("%d\n",arr[j]-arr[i-1]);
//	}
//}