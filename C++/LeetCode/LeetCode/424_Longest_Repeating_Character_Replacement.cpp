#include <queue>
#include <string>
using namespace std;
class Solution {
public:
	int characterReplacement(string s, int k) {
		int ret = 0;

		for (int i = 0; i<26; i++) {
			char cur = 'A' + i;
			int cur_length = 0;
			int not_used = k;
			queue<int> index;
			for (int j = 0; j<s.size(); j++) {
				if (s[j] == cur) {
					cur_length++;
					ret = max(ret, cur_length);
				}
				else {
					if (not_used > 0) {
						cur_length++;
						index.push(j);
						ret = max(ret, cur_length);
						not_used--;
					}
					else if (!index.empty()) {
						ret = max(ret, cur_length);
						cur_length = j - index.front();
						index.pop();
						index.push(j);
					}
					else {
						ret = max(ret, cur_length);
						cur_length = 0;
					}
				}
			}
			ret = max(ret, cur_length);
		}
		return ret;
	}
};