//#include <iostream>
//#include <vector>
//#include <algorithm>
//using namespace std;
//
//int n, c;
//vector<int> home;
//
//
//void INPUT()
//{
//    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
//    cin >> n >> c;
//    for (int i = 0; i < n; i++)
//    {
//        int x; cin >> x;
//        home.push_back(x);
//    }
//}
//
//
//void SOLVE()
//{
//    sort(home.begin(), home.end());
//
//    int left = 1, right = home[n - 1];
//
//    int ans;
//    while (left <= right)
//    {
//        int mid = (left + right) / 2;
//
//        int setIdx = home[0];//가장 마지막에 설치한 집의 위치
//        int cnt = 1;//가장 왼쪽 집에는 무조건 설치
//        for (int i = 1; i < n; i++)
//        {
//            //공유기로부터 mid 이상 떨어져있다면 설치
//            if (setIdx + mid <= home[i])
//            {
//                setIdx = home[i];
//                cnt++;
//            }
//        }
//
//        if (cnt < c) right = mid - 1;
//        else ans = mid, left = mid + 1;
//    }
//
//    cout << ans;
//}
//
//int main()
//{
//    INPUT();
//    SOLVE();
//}