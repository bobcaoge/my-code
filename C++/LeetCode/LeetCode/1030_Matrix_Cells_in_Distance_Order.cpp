#include <vector>
#include <algorithm>
#include<unordered_map>
using namespace std;
class Solution {
public:

	vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
		vector<vector<int>> ret;
		unordered_map<int, vector<vector<int>>> map;
		int max_dis = 0;
		int distance = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				distance = abs(i - r0) + abs(j - c0);
				max_dis = max(distance, max_dis);
				map[distance].push_back({ i,j });
			}
		}
		for (int i = 0; i <= max_dis; i++) {
			vector<vector<int>> buff = map[i];
			ret.insert(ret.end(), buff.begin(), buff.end());
		}
		return ret;
	}

};