#include <string>
#include<vector>
#include<unordered_map>
#include<unordered_set>
using namespace std;
class Solution {
public:
	bool judge(int year) {
		if (year % 400 == 0 || (year % 100 != 0 && year % 4 == 0)) {
			return true;
		}
		return false;
	}
	int dayOfYear(string date) {
		date = date + "-";
		int start = 0;
		vector<string> nums;
		for (int i = 0; i<date.size(); i++) {
			if (date[i] == '-') {
				nums.push_back(date.substr(start, i - start));
				start = i + 1;
			}
		}
		unordered_set<int> set_31 = { 1,3,5,7,8,10 };
		unordered_set<int> set_30 = { 4,6,9,11 };
		int days = 0;
		for (int i = 1; i<stoi(nums[1]); i++) {
			if (set_31.count(i) == 1) {
				days += 31;
			}
			else if (set_30.count(i) == 1) {
				days += 30;
			}
		}
		if (stoi(nums[1]) > 2) {
			if (judge(stoi(nums[0]))) {
				days += 29;
			}
			else {
				days += 28;
			}
		}
		return days + stoi(nums[2]);
	}
};