#include <iostream>
#include <string>
using namespace std;

int main(){
    string docu, search;
    int cnt = 0;
    
    getline(cin, docu);
    getline(cin, search);
    
    for(int i = 0; i < docu.size(); i++){
        bool index = true;
        for(int j = 0; j < search.size(); j++){
            if(docu[i+j] != search[j]){
                index = false;
                break;
            }
        }
        if(index){
            cnt += 1;
            i += search.size() - 1;
        }
    }
    cout << cnt << endl;
    return 0;
}
