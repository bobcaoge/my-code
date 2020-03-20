#include<vector>
using std::vector;
class Solution {
public:
	vector<bool> prefixesDivBy5(vector<int>& A) {
		vector<bool> ret;
		int sum = 0;
		for (auto num : A) {
			sum <<= 1;
			sum += num;
			if ((sum % 5) == 0) {
				ret.push_back(true);
			}
			else {
				ret.push_back(false);
			}
			sum %= 5;
		}

		return ret;
	}
};