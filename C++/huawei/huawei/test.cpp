#include <iostream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <string>
#include <array>
using namespace std;
int dynamic(int arr[], int len) {
	array<int, 100> dp;
	dp.fill(10000);
	dp[0] = 0;
	for (int i = 0; i <= len; i++) {
		for (int j = 0; j < i; j++) {
			if (arr[j] >= i - j) {
				dp[i] = min(dp[i], dp[j] + 1);
			}
		}
	}
	return dp[len];
}
int main2()
{
	int arr[100];
	string s;
	getline(cin, s);
	s += " ";
	int start = 0;
	int j = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == ' ') {
			arr[j++] = stoi(s.substr(start, i));
			start = i + 1;
		}
	}
	j--;
	//int arr[100] = { 7, 5, 9, 4, 2, 6, 8, 3, 5, 4, 3, 9 };
	int ret = dynamic(arr, j);
	cout << (ret < 1000 ? ret: -1) << endl;;
	
	cin.get();
	return 0;
}
