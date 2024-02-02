//#include <iostream>
//#include <string>
//#include <algorithm>
//
//using namespace std;
//
//int nums[2];
//string s;
//
//int main()
//{
//    cin >> s;
//
//    char start = s[0];
//    // 문자열 전체가 한 종류로만 존재한다면
//    // flag = 1이 된다.
//    bool flag = 0;
//    nums[s[0] - '0']++;
//    for (int i = 1; i < s.length(); i++)
//    {
//        if (start != s[i] && !flag) flag = 1;
//
//        if (s[i] != s[i - 1])
//        {
//            nums[s[i] - '0']++;
//        }
//    }
//    cout << min(nums[0], nums[1]);
//
//    return 0;
//}