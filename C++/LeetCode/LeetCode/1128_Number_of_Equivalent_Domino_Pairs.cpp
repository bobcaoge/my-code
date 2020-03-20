#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
	int numEquivDominoPairs(vector<vector<int>>& dominoes) {
		unordered_map<int, int> m;
		int key = 0;
		for (auto domino : dominoes) {
			key = 0;
			if (domino[0] >= domino[1]) {
				key = domino[0] * 10 + domino[1];
			}
			else {
				key = domino[1] * 10 + domino[0];
			}
			m[key] += 1;
		}
		int ret = 0;
		for (auto it : m) {
			ret += (get<1>(it) - 1)*get<1>(it) / 2;
		}
		return ret;
	}
};