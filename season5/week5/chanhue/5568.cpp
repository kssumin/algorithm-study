#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	int n, k, c;
	vector<string> arr; //next_permutation은 컨테이너를 사용(벡터,집합) >반복자 사용가능한 요소
	set<string> ans;
	cin >> n >> k;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		arr.push_back(s);
	}
	sort(arr.begin(), arr.end());
	// next_permutation >> n개 원소의 순열을 구하는 함수 (오름차순 정렬 후 사용해야함)
	do{
		s = "";
		for(int i = 0;i < k; i++) {
			s += arr[i];
		}
		ans.insert(s);
	}while(next_permutation(arr.begin(), arr.end()));
	cout << ans.size();
}