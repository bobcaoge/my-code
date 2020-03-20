#include<vector>
using namespace std;
class Solution {
public:
	void duplicateZeros(vector<int>& arr) {
		vector<int> bak(arr);
		arr.clear();
		for (int i = 0; arr.size()<bak.size(); i++) {
			if (bak[i] == 0) {
				arr.push_back(0);
				if (arr.size() < bak.size()) {
					arr.push_back(0);
				}
				else {
					break;
				}
			}
			else {
				arr.push_back(bak[i]);
			}
		}
	}
};