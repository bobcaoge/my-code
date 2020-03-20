#include <string>
using namespace std;
class Solution {
public:
	string defangIPaddr(string address) {
		string ret = "";
		for (auto c : address) {
			if (c == '.') {
				ret.append("[.]");
			}
			else {
				ret.append(string(1, c));
			}
		}
		return ret;
	}
};