#include <string>
#include <map>
#include<iostream>
#include<algorithm>
#include<vector>
#include<tuple>
using namespace std;
class Solution {
public:
	string longestDiverseString(int a, int b, int c) {
		vector<tuple<int, char>> data = { {a, 'a'}, {b, 'b'}, {c,'c'} };
		sort(data.begin(), data.end());


	}
};