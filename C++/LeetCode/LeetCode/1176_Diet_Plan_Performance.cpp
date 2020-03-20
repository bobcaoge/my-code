#include <vector>
using namespace std;
class Solution {
public:
	int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {

		int ret = 0;
		int window = 0;
		for (int i = 0; i<k - 1; i++) {
			window += calories[i];
		}
		for (int i = k - 1; i<calories.size(); i++) {
			window += calories[i];
			if (window < lower) {
				ret -= 1;
			}
			else if (window > upper) {
				ret += 1;
			}
			window -= calories[i + 1 - k];
		}
		return ret;
	}
};