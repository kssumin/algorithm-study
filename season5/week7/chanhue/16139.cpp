//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int main() {
//	int q, l, r;
//	string S;
//	char a;
//	int ans[27][200001] = { 0, };
//	cin >> S >> q;
//    ans[S[0] - 'a'][0] = 1;
//    for (int i = 1; i < S.size(); i++)
//    {
//        for (int j = 0; j < 27; j++)
//        {
//            ans[j][i] = ans[j][i - 1];
//        }
//        ans[S[i] - 'a'][i]++;
//    }
//    for (int i = 0; i < q; i++)
//    {
//        cin >> a >> l >> r;
//        int temp = a - 'a';
//        if (l == 0)
//            cout << ans[a - 'a'][r] << '\n';
//        else
//            cout << ans[a - 'a'][r] - ans[a - 'a'][l - 1] << '\n';
//    }
//}