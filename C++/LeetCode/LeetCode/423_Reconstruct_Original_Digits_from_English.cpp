#include <string>
#include <vector>
using std::string;
using std::vector;
class Solution {
public:
	string originalDigits(string s) {
		vector<int> record(26, 0);
		for (auto c : s) {
			record[c - 'a'] += 1;
		}
		vector<int> nums(10, 0);
		nums[4] = record['u' - 'a'];
		nums[5] = record['f' - 'a'] - record['u' - 'a'];
		nums[6] = record['x' - 'a'];
		nums[7] = record['s' - 'a'] - record['x' - 'a'];
		nums[8] = record['g' - 'a'];
		nums[9] = record['i' - 'a'] - nums[5] - nums[6] - nums[8];
		nums[1] = record['n' - 'a'] - nums[7] - 2 * nums[9];
		nums[0] = record['z' - 'a'];
		nums[2] = record['w' - 'a'];
		nums[3] = record['t' - 'a'] - nums[2] - nums[8];
		string ret = "";
		for (int i = 0; i<nums.size(); i++) {
			if (nums[i] > 0) {
				ret += string(nums[i], '0' + i);
			}
		}
		return ret;

	}
};