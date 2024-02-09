//#include<iostream>
//using namespace std;
//
//int cnt_1 = 0, cnt0 = 0, cnt1 = 0;
////	각각 -1이 적힌 종이, 0이 적힌 종이, 1이 적힌 종이의 개수를 나타내는 변수
//int arr[2200][2200];
//
//bool issame(int y, int x, int n) {		//	종이 내의 숫자들을 체크하는 함수
//	int num = arr[y][x];
//	for (int i = y; i < y + n; i++) {
//		for (int j = x; j < x + n; j++) {
//			if (num != arr[i][j]) {
//				return false;
//			}
//		}
//	}
//	return true;
//}
//
//void div(int y, int x, int n) {
//	if (issame(y, x, n)) {		//	종이 내의 숫자가 모두 같다면(true)
//		if (arr[y][x] == -1) {
//			cnt_1++;
//		}
//		else if (arr[y][x] == 0) {
//			cnt0++;
//		}
//		else if (arr[y][x] == 1) {
//			cnt1++;
//		}
//	}
//	else {		//	종이 내의 숫자가 하나라도 다르다면(false)
//		int volume = n / 3;		//	한 변의 길이를 1/3
//		for (int i = 0; i < 3; i++) {		//	분할하면 한 변마다 3번씩만 반복
//			for (int j = 0; j < 3; j++) {
//				div(volume * i + y, volume * j + x, volume);
//				//	1/3을 한 한 변의 길이와 분할했을 때의 위치 경우의 수들을 전달해서
//					  //	또 숫자가 다르다면 계속 분할하는 형식임
//			}
//		}
//	}
//}
//
//int main(void) {
//	int n;
//	cin >> n;
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < n; j++) {
//			cin >> arr[i][j];
//		}
//	}
//	div(0, 0, n);		//	처음 파라미터
//	cout << cnt_1 << '\n' << cnt0 << '\n' << cnt1;
//	return 0;
//}