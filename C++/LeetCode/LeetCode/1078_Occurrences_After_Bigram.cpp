#include <vector>
#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
	vector<string> findOcurrences(string text, string first, string second) {
		vector<string> words;
		int start = 0;
		int len = 0;
		for (int i = 0; i<text.size(); i++) {
			if (text[i] != ' ') {
				len++;
			}
			else {
				words.push_back(text.substr(start, len));
				start = i + 1;
				len = 0;
			}
		}
		words.push_back(text.substr(start, len));

		bool flag_of_first = false;
		vector<string> ret;
		for (int i = 0; i<words.size(); i++) {
			if (flag_of_first && words[i] == second && i + 1 < words.size()) {
				ret.push_back(words[i + 1]);
			}
			if (words[i] == first) {
				flag_of_first = true;
			}
			else {
				flag_of_first = false;
			}
		}
		return ret;
	}
};