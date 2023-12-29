//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//int main() {
//	int n, k;
//	string str;
//	queue<int> que[21];
//	long long ans = 0;
//
//	cin >> n >> k;
//	for (int i = 0; i < n; i++) {
//
//		cin >> str;
//
//		int len = str.length(); //이름의 길이
//
//		while (!que[len].empty() && i - que[len].front() > k) { //이름의 길이에 맞는 큐가 비어있지않고 등수 차이가 k보다 크면
//			que[len].pop();									 //맨 앞에있는 애 빼기
//		}
//		ans += que[len].size(); //큐에 들어있는 개수 더하기
//		que[len].push(i);
//
//	}
//
//	cout << ans;
//}