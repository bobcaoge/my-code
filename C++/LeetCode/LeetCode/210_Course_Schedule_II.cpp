#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool flag = true;
    vector<int> ret;
    vector<int> visited;
    unordered_map<int, vector<int>> graph;
    bool dfs(int i){
        if(visited[i] == -1){
            flag = false;
            return false; 
        }
        if(visited[i] == 1){
            return true;
        }
        visited[i] = -1;
        for(auto vertex: graph[i]){
            if(!dfs(vertex)){
                return false;
            }
        }
        visited[i] = 1;
        ret.push_back(i);
        return true;
    }
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        graph.clear();
        ret.clear();
        visited = vector<int>(numCourses, 0);
        for(auto edge: prerequisites){
            graph[edge[1]].push_back(edge[0]);
        }
        for(int i=0;i<numCourses;i++){
            if(!dfs(i)){
                return {};
            }
        }
        return vector<int>(ret.rbegin(), ret.rend());
    }
};