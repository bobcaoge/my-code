#include <vector>
using namespace std;

class Solution {
public:
	int countBattleships(vector<vector<char>>& board) {
		int ret = 0;
		int row = board.size();
		if (row == 0) {
			return 0;
		}
		int column = board[0].size();
		for (int i = 0; i<row; i++) {
			for (int j = 0; j<column; j++) {
				if (board[i][j] == 'X') {
					if (j == column - 1 && i == row - 1) {
						ret += 1;
					}
					else if (j == column - 1) {
						if (board[i + 1][j] == '.')
							ret += 1;
					}
					else if (i == row - 1) {
						if (board[i][j + 1] == '.')
							ret += 1;
					}
					else {
						if (board[i][j + 1] == '.' && board[i + 1][j] == '.')
							ret += 1;
					}
				}
			}
		}
		return ret;
	}
};