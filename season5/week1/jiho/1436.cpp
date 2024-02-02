#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    int cnt = 0;
    cin >> n;

    for (int i = 666;;++i) {
        string str_num = to_string(i);
        if (str_num.find("666") != string::npos) {
            cnt += 1;

            if (cnt == n) {
                cout << i << endl;
                break;
            }
        }
    }

    return 0;
}
