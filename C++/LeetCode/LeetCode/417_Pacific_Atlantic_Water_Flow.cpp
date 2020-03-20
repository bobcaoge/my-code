#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
	void dfs(vector<vector<int>>& matrix, int i, int j, int row, int column, unordered_set<int>& coll) {
		if (coll.count(i * 1000 + j) == 1) {
			return;
		}
		coll.insert(i * 1000 + j);
		for (int di = -1; di < 2; di++) {
			for (int dj = -1; dj < 2; dj++) {
				if (abs(di) + abs(dj) == 1 && i + di >= 0 && i + di < row && j + dj >= 0 && j + dj < column) {
					if (matrix[i + di][j + dj] >= matrix[i][j]) {
						dfs(matrix, i + di, j + dj, row, column, coll);
					}
				}
			}
		}
	}
	vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
		int row = matrix.size();
		if (row == 0) {
			return{};
		}
		int column = matrix[0].size();
		vector<vector<int>> ret;
		unordered_set<int> specific;
		unordered_set<int> atlantic;
		for (int j = 0; j<column; j++) {
			dfs(matrix, 0, j, row, column, specific);
			dfs(matrix, row - 1, j, row, column, atlantic);
		}
		for (int i = 0; i<row; i++) {
			dfs(matrix, i, 0, row, column, specific);
			dfs(matrix, i, column - 1, row, column, atlantic);
		}
		for (auto it = specific.begin(); it != specific.end(); it++) {
			if (atlantic.count(*it) == 1) {
				ret.push_back(vector<int>{(*it) / 1000, (*it) % 1000});
			}
		}
		return ret;
	}
};