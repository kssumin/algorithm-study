#include <iostream>
#include <vector> 

using namespace std;

int N, M;
int arr[8];
bool H[8];

void nHm(int HN)
{
	if (HN == M)
	{
		for (int i = 0; i < M; i++)
			cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	for (int i = 1; i <= N; i++)
	{
		arr[HN] = i;
		nHm(HN + 1);
	}
}
int main(void)
{
	cin >> N >> M;
	nHm(0);
	return 0;
}
