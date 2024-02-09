//#include <iostream>
//
//using namespace std;
//
//
//long long recur(int a, int b, int c)
//{
//    if (b == 0)
//    {
//        return 1;
//    }
//    if (b == 1)
//    {
//        return a % c;
//    }
//
//    long long temp = recur(a, b / 2, c);
//
//    if (b % 2 == 0)
//    {
//        return temp * temp % c;
//    }
//    else
//    {
//        return a * (temp * temp % c) % c;
//    }
//}
//
//int main()
//{
//    int a, b, c;
//
//    cin >> a >> b >> c;
//    cout << recur(a, b, c);
//
//    return 0;
//}
