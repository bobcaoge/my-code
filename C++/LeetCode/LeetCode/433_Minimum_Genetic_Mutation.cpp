#include<string>
#include <queue>
#include <vector>
using std::vector;
using std::string;
using std::priority_queue;
struct Data {
	int step;
	string start;
	string end;
};
bool operator<(Data first, Data second) {
	return first.step <= second.step;
}
class Solution {
public:
	bool check(string start, string end) {
		int changed = 0;
		for (int i = 0; i<start.size(); i++) {
			if (start[i] != end[i]) {
				changed++;
			}
		}
		return changed == 1;
	}
	int minMutation(string start, string end, vector<string>& bank) {
		priority_queue<Data> heap;
		heap.push({ 0, start, start });
		while (!heap.empty()) {
			Data buff = heap.top();
			heap.pop();
			if (buff.end == end) {
				return -buff.step;
			}
			for (auto s : bank) {
				if (check(s, buff.end) && buff.start != s) {
					heap.push({ buff.step - 1, buff.end, s });
				}
			}
		}
		return -1;
	}
};