#include <vector>
#include <string>
#include <array>
using namespace std;
class Solution {
public:
	int countCharacters(vector<string>& words, string chars) {
		array<int, 26> record;
		record.fill(0);
		for (auto c : chars) {
			record[c - 'a'] += 1;
		}
		array<int, 26> buff;
		int ret = 0;
		bool flag;
		for (auto word : words) {
			buff.fill(0);
			flag = true;
			for (auto c : word) {
				int key = c - 'a';
				buff[key] += 1;
				if (buff[key] > record[key]) {

					flag = false;
					break;
				}
			}
			if (flag) {
				ret += word.size();
			}
		}
		return ret;
	}
};