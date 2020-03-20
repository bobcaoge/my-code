#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
	int lastStoneWeight(vector<int>& stones) {
		int a;
		int b;
		while (stones.size() > 1) {
			sort(stones.begin(), stones.end());
			a = stones.back();
			stones.pop_back();
			b = stones.back();
			stones.pop_back();
			if ((a - b)>0) {
				stones.push_back(a - b);
			}
		}
		if (stones.size() == 0) {
			return 0;
		}
		return stones[0];

	}
	int lastStoneWeight_1(vector<int>& stones) {
		priority_queue<int> q(stones.begin(), stones.end());
		int a;
		int b;
		while (q.size() > 1) {
			a = q.top();
			q.pop();
			b = q.top();
			q.pop();
			if (a>b) {
				q.push(a - b);
			}
		}
		if (q.empty()) {
			return 0;
		}
		return q.top();

	}
};