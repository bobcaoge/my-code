#include<string>
using namespace std;

class Solution {
public:
	string get(string s, int len) {
		string ret = "";
		for (int i = 0; i<len; i++) {
			ret += s;
		}
		return ret;
	}
	string buff(string str1) {
		for (int i = 0; i<str1.size(); i++) {
			if (str1.size() % (i + 1) == 0 && get(str1.substr(0, i + 1), str1.size() / (i + 1)) == str1) {
				return str1.substr(0, i + 1);
			}
		}
		return "";

	}
	string gcdOfStrings(string str1, string str2) {
		if (str1 == str2) {
			return str1;
		}
		string a = buff(str1);
		string b = buff(str2);
		if (a != b || a == "" || b == "") {
			return "";
		}
		int len_a = str1.size() / a.size();
		int len_b = str2.size() / a.size();
		int temp = 0;
		while (len_a % len_b != 0) {
			temp = len_a % len_b;
			len_a = len_b;
			len_b = temp;
		}
		string ret = "";
		for (int i = 0; i<len_b; i++) {
			ret += a;
		}
		return ret;

	}
};