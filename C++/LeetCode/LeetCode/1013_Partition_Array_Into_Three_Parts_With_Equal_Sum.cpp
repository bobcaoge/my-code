#include<vector>
using std::vector;
class Solution {
public:
	bool canThreePartsEqualSum(vector<int>& A) {
		int sum = 0;
		for (auto num : A) {
			sum += num;
		}
		if (sum % 3 != 0) {
			return false;
		}
		int sum_after_partition = sum / 3;
		int flag = 0;
		int cur_sum = 0;
		for (auto num : A) {
			cur_sum += num;
			if (cur_sum == sum_after_partition) {
				flag += 1;
				if (flag == 2) {
					return true;
				}
				cur_sum = 0;
			}
		}
		return false;
	}
};