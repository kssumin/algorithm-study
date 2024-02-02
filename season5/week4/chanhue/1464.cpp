//#include <iostream>
//#include <string>
//#include <deque>
//
//using namespace std;
//
//int main() {
//	deque<char> slist;
//	string s;
//	cin >> s;
//	slist.push_back(s[0]);
//	for (int i = 1; i < s.length(); i++) {
//		if (slist.front() < s[i]) {
//			slist.push_back(s[i]);
//		}
//		else {
//			slist.push_front(s[i]);
//		}
//	}
//	while(!slist.empty()) {
//		cout << slist.front();
//		slist.pop_front();
//	}
//}