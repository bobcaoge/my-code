#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
	static bool cmp(vector<int>& a, vector<int>& b) {
		if (a[0] < b[0]) {
			return true;
		}
		else if (a[0] == b[0]) {
			if (a[1] <= b[1]) {
				return true;
			}
			return false;
		}
		return false;
	}
	int eraseOverlapIntervals(vector<vector<int>>& intervals) {
		sort(intervals.begin(), intervals.end(), cmp);
		int ret = 0;
		if (intervals.size() == 0) {
			return 0;
		}
		vector<int> old = intervals[0];
		for (int i = 1; i<intervals.size(); i++) {
			if (intervals[i][0] >= old[1]) {
				old = intervals[i];
			}
			else {
				if (intervals[i][1] < old[1]) {
					old = intervals[i];

				}
				ret++;
			}
		}
		return ret;
	}
};