//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int main() {
//	int n;
//	int d[1001];
//	int cnt1[1001];
//	int cnt2[1001];
//	int cnt3[1001];
//	int ans = 0;
//
//	cin >> n;
//	for (int i = 0; i < n; i++)
//		cin >> d[i];
//
//	for (int i = 0; i < n; i++) {
//		cnt1[i] = 1;
//		for (int j = 0; j < i; j++) {
//			if (d[i] > d[j]) {
//				cnt1[i] = max(cnt1[i], cnt1[j] + 1);
//			}
//		}
//	}
//
//	for (int i = n - 1; i >= 0; i--) {
//		cnt2[i] = 1;
//		for (int j = n - 1; j > i; j--) {
//			if (d[i] > d[j]) {
//				cnt2[i] = max(cnt2[i], cnt2[j] + 1);
//			}
//		}
//	}
//	for (int i = 0; i < n; i++) {
//		cnt3[i] = cnt1[i] + cnt2[i];
//		ans = max(ans, cnt3[i]);
//	}
//
//	cout << ans - 1 << endl;
//
//	return 0;
//}