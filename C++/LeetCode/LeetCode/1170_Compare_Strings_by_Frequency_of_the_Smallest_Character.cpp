#include <string>
#include <vector>
#include <array>
using namespace std;

class Solution {
public:
	int f(string word) {
		int ret = 0;
		char cur = 'z';
		for (auto c : word) {
			if (c == cur) {
				ret++;
			}
			else if (c < cur) {
				cur = c;
				ret = 1;
			}
		}
		return ret;
	}
	array<int, 2000> get_frequencies_of_words(vector<string> words) {
		array<int, 2000> arr;
		arr.fill(0);
		for (auto word : words) {
			arr[f(word)]++;
		}
		for (int i = arr.size() - 2; i >= 0; i--) {
			arr[i] += arr[i + 1];
		}
		return arr;
	}
	vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
		vector<int> ret;
		array<int, 2000> arr = get_frequencies_of_words(words);
		for (int i = 0; i<queries.size(); i++) {
			ret.push_back(arr[f(queries[i]) + 1]);
		}
		return ret;
	}
};