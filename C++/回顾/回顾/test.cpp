#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;
class Solution {
public:
	vector<string> commonChars(vector<string>& A) {
		map<char, int> m;

		for (char c : A[0]) {
			m[c] += 1;
		}
		for (string s : A) {
			map<char, int> buff;
			for (char c : s) {
				if ( m[c] > 0){
					buff[c] += 1;
					m[c] -= 1;
				}
			}
			m = buff;
		}
		vector<string> ret;
		for (auto it = m.begin(); it != m.end(); it++) {
			for (int i = 0; i < it->second; i++) {
				ret.push_back(string(1, it->first));
			}
		}
		return ret;

	}
};