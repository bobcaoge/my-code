#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
	vector<int> minSubsequence(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		int sum = 0;
		for_each(nums.begin(), nums.end(), [&sum](int a) {sum += a; });
		vector<int> ret;
		int cur_sum = 0;
		for (auto it = nums.rbegin(); it != nums.rend(); it++) {
			ret.push_back(*it);
			cur_sum += *it;
			if (cur_sum > sum - cur_sum) break;
		}
		sort(ret.begin(), ret.end(), [](int a, int b) {return a > b; });
		return ret;

	}
};