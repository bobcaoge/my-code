#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <iostream>
using namespace std;
class Solution {
public:
	vector<string> ret;
	bool dfs(unordered_map<string, multiset<string>>& graph, int num_of_edges, string cur) {
		//cout << cur << " " << ret.size() << endl;
		if (ret.size() == num_of_edges + 1) {
			return true;
		}
		set<string> buff(graph[cur].begin(), graph[cur].end());
		for (auto next : buff) {
			ret.push_back(next);
			graph[cur].erase(graph[cur].find(next));
			if (dfs(graph, num_of_edges, next)) {
				return true;
			}
			graph[cur].insert(next);
			ret.pop_back();
		}
		return false;

	}
	vector<string> findItinerary(vector<vector<string>>& tickets) {
		unordered_map<string, multiset<string>> graph;
		for (auto ticket : tickets) {
			graph[ticket[0]].insert(ticket[1]);
		}
		ret.clear();
		ret.push_back("JFK");
		dfs(graph, tickets.size(), "JFK");
		if (ret.size() > 1) {
			return ret;
		}
		return{};
	}
};
int main_test() {
	Solution s;
	vector<vector<string>> edges ={{"EZE","AXA"},{"TIA","ANU"},{"ANU","JFK"},{"JFK","ANU"},{"ANU","EZE"},{"TIA","ANU"},{"AXA","TIA"},{"TIA","JFK"},{"ANU","TIA"},{"JFK","TIA"}}; 
	auto ret = s.findItinerary(edges);
	for (auto buff : ret) {
		cout << buff << " ";
	}
	cout << endl;
	cin.get();
	return 0;
}