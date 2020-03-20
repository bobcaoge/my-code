#include<vector>
using namespace std;
class Node {
public:
	bool val;
	bool isLeaf;
	Node* topLeft;
	Node* topRight;
	Node* bottomLeft;
	Node* bottomRight;

	Node() {}

	Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
		val = _val;
		isLeaf = _isLeaf;
		topLeft = _topLeft;
		topRight = _topRight;
		bottomLeft = _bottomLeft;
		bottomRight = _bottomRight;
	}
};
class Solution {
public:
	bool check(vector<vector<int>>& grid, int left, int right, int top, int down) {
		bool flag = grid[top][left] == 1;
		for (int i = top; i <= down; i++) {
			for (int j = left; j <= right; j++) {
				if (flag != (grid[i][j] == 1)) {
					return false;
				}
			}
		}
		return true;
	}
	Node* buff(vector<vector<int>>& grid, int left, int right, int top, int down) {
		if (check(grid, left, right, top, down)) {
			return new Node(grid[top][left] == 1, true, NULL, NULL, NULL, NULL);
		}
		else {
			Node* cur = new Node(false, false, NULL, NULL, NULL, NULL);
			int middle_of_left_right = (left + right) / 2;
			int middle_of_top_down = (top + down) / 2;
			cur->topLeft = buff(grid, left, middle_of_left_right, top, middle_of_top_down);
			cur->topRight = buff(grid, middle_of_left_right + 1, right, top, middle_of_top_down);

			cur->bottomLeft = buff(grid, left, middle_of_left_right, middle_of_top_down + 1, down);
			cur->bottomRight = buff(grid, middle_of_left_right + 1, right, middle_of_top_down + 1, down);
			return cur;
		}
	}
	Node* construct(vector<vector<int>>& grid) {
		return buff(grid, 0, grid.size() - 1, 0, grid[0].size() - 1);
	}
};



