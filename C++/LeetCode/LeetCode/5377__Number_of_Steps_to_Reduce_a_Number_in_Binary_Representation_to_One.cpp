#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
	int numSteps(string s) {
		int ret = 0;
		int carry = 0;
		int cur = 0;
		for (int i = s.size() - 1; i > 0; i--) {
			if (s[i] == '0') {
				if (carry == 0) {
					ret++;
				}
				else {
					ret += 2;
				}
			}
			else {
				if (carry == 0) {
					ret += 2;
					carry = 1;
				}
				else {
					ret += 1;
				}
			}
		}
		return ret + (carry == 0 ? 1 : 2)-1;
		
		

	}
};
int mainfadfahdfvg() {
	Solution s;
	cout << s.numSteps("1101") << endl;
	cout << s.numSteps("10");
	cin.get();
	return 0;
}