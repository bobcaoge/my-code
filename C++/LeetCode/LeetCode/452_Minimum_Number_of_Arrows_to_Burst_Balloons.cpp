#include<vector>
#include<iostream>
#include<algorithm>
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
	int findMinArrowShots(vector<vector<int>>& points) {

		sort(points.begin(), points.end(), cmp);
		int ret = 0;
		if (points.size() == 0) {
			return 0;
		}
		vector<int> old = points[0];
		for (int i = 1; i<points.size(); i++) {
			if (points[i][0] > old[1]) {
				old = points[i];
			}
			else {
				if (points[i][1] < old[1]) {
					old = points[i];
				}
				ret++;
			}
		}
		return points.size() - ret;
	}
};