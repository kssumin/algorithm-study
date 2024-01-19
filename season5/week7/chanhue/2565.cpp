#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, res = 0;
vector<pair<int, int>> v;
int dp[100];

void solution() {
	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (v[j].second < v[i].second) {
				dp[i] = max(dp[i], dp[j] + 1);
			}
		}

		res = max(res, dp[i]);
	}

	cout << n - res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		v.push_back({ a,b });
	}

	solution();

	return 0;
}