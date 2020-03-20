#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
	vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
		unordered_map<int, int> m;
		unordered_set<int> check(arr2.begin(), arr2.end());
		vector<int> other;
		for (auto num : arr1) {
			if (check.count(num) == 1) {
				m[num] += 1;
			}
			else {
				other.push_back(num);
			}
		}
		vector<int> ret;
		for (auto num : arr2) {
			vector<int> to_insert(m[num], num);
			ret.insert(ret.end(), to_insert.begin(), to_insert.end());
		}
		sort(other.begin(), other.end());
		ret.insert(ret.end(), other.begin(), other.end());
		return ret;

	}
};