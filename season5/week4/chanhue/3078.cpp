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
//		int len = str.length(); //�̸��� ����
//
//		while (!que[len].empty() && i - que[len].front() > k) { //�̸��� ���̿� �´� ť�� ��������ʰ� ��� ���̰� k���� ũ��
//			que[len].pop();									 //�� �տ��ִ� �� ����
//		}
//		ans += que[len].size(); //ť�� ����ִ� ���� ���ϱ�
//		que[len].push(i);
//
//	}
//
//	cout << ans;
//}