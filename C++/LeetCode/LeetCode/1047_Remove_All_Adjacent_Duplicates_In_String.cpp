#include<string>
#include<stack>
#include<iostream>
using namespace std;
class Solution {
public:
	string removeDuplicates(string S) {
		char old = '\n';
		stack<char> sta;
		for (auto c : S) {
			if (sta.empty()) {
				sta.push(c);
			}
			else {
				if (sta.top() == c) {
					sta.pop();
				}
				else {
					sta.push(c);
				}
			}
		}
		string s = "";
		while (!sta.empty()) {
			s = string(1, sta.top()) + s;
			sta.pop();
		}
		return s;
	}
	string removeDuplicates_1(string S) {
		char old = '\n';
		string s = "";
		for (auto c : S) {
			if (s.size() == 0) {
				s += string(1, c);
			}
			else {
				if (c == s.back()) {
					s.pop_back();
				}
				else {
					s += string(1, c);
				}
			}
		}
		return s;
	}
};