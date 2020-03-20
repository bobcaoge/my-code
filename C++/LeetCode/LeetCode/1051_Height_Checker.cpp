#include <vector>
using namespace std;
#include <algorithm>
class Solution {
public:
	int heightChecker(vector<int>& heights) {
		vector<int> buff(heights);
		sort(buff.begin(), buff.end());
		int ret = 0;
		for (int i = 0; i<heights.size(); i++) {
			if (buff[i] != heights[i]) {
				ret++;
			}
		}
		return ret;
	}
};