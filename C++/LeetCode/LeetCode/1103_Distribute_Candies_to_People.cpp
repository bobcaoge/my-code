#include <vector>
using namespace std;
class Solution {
public:
	vector<int> distributeCandies(int candies, int num_people) {
		int n = int(sqrt(candies * 2));
		if (n*(n + 1) > 2 * candies) {
			n--;
		}
		vector<int> ret(num_people, 0);
		for (int i = 0; i<num_people; i++) {
			int len = int(n / num_people) + (n%num_people >= i + 1);
			int a0 = i + 1;
			int an = a0 + (len - 1)*num_people;
			ret[i] = (a0 + an)*len / 2;
		}
		ret[n%num_people] += candies - (1 + n)*n / 2;
		return ret;
	}
};