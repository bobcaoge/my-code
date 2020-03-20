#include <iostream>
#include <string>
#include <array>
#include <vector>
#include <algorithm>
#include <time.h>
#include<random>
#include < unordered_map>
#include<unordered_set>
using namespace std;
class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) {
		unordered_map<int, int> m;
		unordered_set<int> keys;
		for (auto num : nums) {
			m[num] += 1;
			keys.insert(num);
		}
		unordered_set<int> s;
		vector<vector<int>> ret;
		for (auto k : keys) {
			m[k] -= 1;
			s.clear();
			for (auto it = m.begin(); it != m.end(); it++) {
				int value = it->second;
				int key = it->first;
				if (value == 0 || s.count(key) > 0) {
					continue;
				}
				m[key] -= 1;
				if (m[-k - key] > 0) {
					ret.push_back({ k, key, -k - key });
					s.insert(-k - key);
				}
				m[key] += 1;
			}
			m.erase(k);
		}
		return ret;

	}
};
int mainaa() {
	Solution s;
	vector<int> a = { -1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4 };
	s.threeSum(a);
	cin.get();
	return 0;
}