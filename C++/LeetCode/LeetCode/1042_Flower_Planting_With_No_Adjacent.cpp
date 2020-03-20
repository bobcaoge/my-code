#include<vector>
#include<unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
	vector<int> gardenNoAdj(int N, vector<vector<int>>& paths) {
		unordered_map<int, vector<int>> m;
		for (auto path : paths) {
			m[path[0]].push_back(path[1]);
			m[path[1]].push_back(path[0]);
		}
		vector<int> ret;
		unordered_set<int> set;
		vector<int> disjoins;
		for (int i = 1; i <= N; i++) {
			disjoins = m[i];
			for (auto disjoin : disjoins) {
				if (disjoin <= ret.size()) {
					set.insert(ret[disjoin - 1]);
				}
			}
			for(int i=1;i<=4;i++){
				if (set.count(i) == 0) {
					ret.push_back(i);
					break;
				}
			}
			set.clear();
			
		}
		return ret;


	}
};