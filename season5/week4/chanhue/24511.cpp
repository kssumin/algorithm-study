//#include <iostream>
//#include <queue>
//#include <stack>
//using namespace std;
//stack <int> st;
//queue <int> q;
//bool QueueStack[100000];
//int main() {
//    int N, M, input, x;
//    cin >> N;
//    for (int i = 0; i < N; i++)
//    {
//        cin >> QueueStack[i];
//    }
//    for (int i = 0; i < N; i++)
//    {
//        cin >> input;
//        if (QueueStack[i] == 0)
//        {
//            st.push(input);
//        }
//    }
//    while (!st.empty())
//    {
//        q.push(st.top());
//        st.pop();
//    }
//    cin >> M;
//    for (int i = 0; i < M; i++)
//    {
//        cin >> input;
//        q.push(input);
//    }
//    for (int i = 0; i < M; i++)
//    {
//        cout << q.front() << " ";
//        q.pop();
//    }
//}