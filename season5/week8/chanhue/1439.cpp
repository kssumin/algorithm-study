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
//    // ���ڿ� ��ü�� �� �����θ� �����Ѵٸ�
//    // flag = 1�� �ȴ�.
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