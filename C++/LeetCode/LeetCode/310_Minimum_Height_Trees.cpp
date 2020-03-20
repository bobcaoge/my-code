#include <vector>
#include <unordered_set>
using namespace std;
class Solution {
public:
	vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {

		vector<unordered_set<int>> graph(n, unordered_set<int>());
		for (auto edge : edges) {
			graph[edge[0]].insert(edge[1]);
			graph[edge[1]].insert(edge[0]);
		}
		vector<int> leaves;
		for (int i = 0; i<graph.size(); i++) {
			if (graph[i].size() == 1) {
				leaves.push_back(i);
			}
		}
		if (n == 1) {
			return{ 0 };
		}
		while (true) {
			vector<int> next;
			for (auto leave : leaves) {
				for (auto neighbor : graph[leave]) {
					graph[neighbor].erase(leave);
					if (graph[neighbor].size() == 1) {
						next.push_back(neighbor);
					}
				}
			}
			if (next.empty()) {
				return leaves;
			}
			leaves = next;
		}
	}
};