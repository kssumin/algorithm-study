#include <iostream>
#include <string>
using namespace std;

bool find_square(char rect[51][51], int N, int M, int a){
    for(int i = 0; i < N - a; i++){
        for(int j = 0; j < M - a; j++){
            char s = rect[i][j];
            if(s == rect[i][j] && s == rect[i][j+a] && s == rect[i+a][j] && s == rect[i+a][j+a])
                return true;
        }
    }
    return false;
}

int main(){
    char rect[51][51];
    int N, M;
    cin >> N >> M;
    
    int a = N < M ? N : M;
    for(int i = 0; i < N; i++){
        cin >> rect[i];
    }
    while(a-- && !find_square(rect, N, M, a));
    cout << (a+1)*(a+1) << endl;
    
    return 0;
}
