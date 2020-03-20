#include<vector>
using namespace std;
class Solution {
public:
	vector<int> findDuplicates(vector<int>& nums) {
		int temp;
		for (int i = 0; i<nums.size(); i++) {
			while (nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]) {
				temp = nums[nums[i] - 1];
				nums[nums[i] - 1] = nums[i];
				nums[i] = temp;
			}
		}
		vector<int> ret;

		for (int i = 0; i<nums.size(); i++) {
			if (nums[i] != i + 1) {
				ret.push_back(nums[i]);
			}
		}
		return ret;
	}
};