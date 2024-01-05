#include<iostream>
#include<stack>

using namespace std;

int main() {
	stack<int> big;
	int nge[1000001], inp[1000001];
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> inp[i];
	}
	for (int i = N - 1; i >= 0; i--)
	{
		while (!big.empty() && big.top() <= inp[i]) {
			big.pop();
		}

		if (big.empty()) {
			nge[i] = -1;
		}
		else nge[i] = big.top();

		big.push(inp[i]);
	}
	for (int i = 0; i < N; i++) {
		cout << nge[i] << " ";
	}
}