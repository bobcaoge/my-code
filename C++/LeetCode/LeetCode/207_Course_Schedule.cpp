#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
	bool dfs(int i, vector<int>& visited, unordered_map<int, vector<int>>& graph) {
		if (visited[i] == -1) {
			return false;
		}
		if (visited[i] == 1) {
			return true;
		}
		visited[i] = -1;
		for (auto vertex : graph[i]) {
			if (!dfs(vertex, visited, graph)) {
				return false;
			}
		}
		visited[i] = 1;
		return true;
	}

	bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
		unordered_map<int, vector<int>> graph;
		vector<int> visited(numCourses, 0);
		for (auto edge : prerequisites) {
			graph[edge[0]].push_back(edge[1]);
		}
		for (int i = 0; i < numCourses; i++) {
			if (!dfs(i, visited, graph)) {
				return false;
			}
		}
		return true;

	}
};



