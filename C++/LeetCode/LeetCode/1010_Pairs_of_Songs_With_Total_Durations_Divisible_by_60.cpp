#include<iostream>
#include<vector>
using namespace std;
#include<map>
class Solution {
public:
	int numPairsDivisibleBy60(vector<int>& time) {
		int ret = 0;
		map<int, int> m;
		for (auto t : time) {
			m[t % 60] = m[t % 60] + 1;
		}
		for (auto t : time) {
			t %= 60;
			m[t] -= 1;
			ret += m[60 - t];
			m[t] += 1;
		}
		return ret / 2 + (m[0] * (m[0] - 1)) / 2;
		/*
		method 2
		array<int, 60> arr={0};
		for (auto t: time){
			arr[t%60] += 1;
		}
		int ret = 0;
		for (int i=1;i<30;i++){
			ret += arr[i]*arr[60-i];
		}
		return ret+arr[0]*(arr[0]-1)/2 + arr[30]*(arr[30]-1)/2;
		*/
	}
};