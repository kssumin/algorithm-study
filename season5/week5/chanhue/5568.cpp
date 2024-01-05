#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	int n, k, c;
	vector<string> arr; //next_permutation�� �����̳ʸ� ���(����,����) >�ݺ��� ��밡���� ���
	set<string> ans;
	cin >> n >> k;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		arr.push_back(s);
	}
	sort(arr.begin(), arr.end());
	// next_permutation >> n�� ������ ������ ���ϴ� �Լ� (�������� ���� �� ����ؾ���)
	do{
		s = "";
		for(int i = 0;i < k; i++) {
			s += arr[i];
		}
		ans.insert(s);
	}while(next_permutation(arr.begin(), arr.end()));
	cout << ans.size();
}