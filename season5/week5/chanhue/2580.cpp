#include <iostream>
#include <utility>
#include <vector>
using namespace std;
int board[9][9]; // ������ ���� ����
vector<pair<int, int>> points; // ��ĭ�� ��ġ ����
int cnt = 0;
bool found = false; // ������ �� �ϼ� �÷���
bool check(pair<int, int> p)
{
    int square_x = p.first / 3; // ������ ����
    int square_y = p.second / 3;
    for (int i = 0; i < 9; i++)
    {
        if (board[p.first][i] == board[p.first][p.second] && i != p.second)
            return false; // ���� �࿡ ���� ���ڰ� ������ false ��ȯ
        if (board[i][p.second] == board[p.first][p.second] && i != p.first)
            return false; // ���� ���� ���� ���ڰ� ������ false ��ȯ
    }
    for (int i = 3 * square_x; i < 3 * square_x + 3; i++)
        for (int j = 3 * square_y; j < 3 * square_y + 3; j++)
        {
            if (board[i][j] == board[p.first][p.second])
            {
                if (i != p.first && j != p.second)
                    return false; // ���� ������ ���� ���ڰ� ������ false ��ȯ
            }
        }
    return true; // ��� ���� ������ ��ȿ�� �˻� ���
}
void sudoku(int N) {
    if (N == cnt) // ��ĭ�� ������ŭ�� ä���� ������ ���� �ϼ��Ǹ�
    {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++)
                cout << board[i][j] << ' ';
            cout << '\n';
        } // ��� ���
        found = true; // �÷��� true�� ����
        return;
    }
    for (int j = 1; j <= 9; j++)
    {
        board[points[N].first][points[N].second] = j; // 1~9 ������ ���ڸ� �־
        if (check(points[N])) // ����� ��ȿ�ϸ� ���� ��ĭ�� ä�췯 ��
            sudoku(N + 1);
        if (found) // ������ �ϼ�������� �� �̻� �ٸ� �ظ� ã�� �ʿ䰡 �����Ƿ� �Լ� ����
            return;
    }
    board[points[N].first][points[N].second] = 0;// �����ظ� ��ã���� ��� �� ����ֱ�
    return;
}
int main() {
    pair<int, int> point;
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == 0)
            {
                cnt++;
                point.first = i;
                point.second = j;
                points.push_back(point); // ��ĭ�� ��ǥ ����
            }
        }
    sudoku(0);
}