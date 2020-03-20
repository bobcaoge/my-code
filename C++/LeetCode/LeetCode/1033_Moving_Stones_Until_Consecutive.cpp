#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;
class Solution {
public:
	vector<int> numMovesStones(int a, int b, int c) {
		int sum = a + b + c;
		int min_num = min(min(a, b), c);
		int max_num = max(max(a, b), c);
		a = min_num;
		c = max_num;
		b = sum - a - c;
		vector<int> ret;
		if (b - a == 1 && c - b == 1) {
			ret.push_back(0);
		}
		else if (b - a == 2 || c - b == 1 || b - a == 1 || c - b == 2) {
			ret.push_back(1);
		}
		else {
			ret.push_back(2);
		}
		ret.push_back(b - a + c - b - 2);
		return ret;

	}
};