#include <sstream>
#include <iostream>
#include <queue>
#include <vector>
#include <array>
#include <math.h>
#include<algorithm>
using namespace std;

int main() {
/*
	vector<int> vec = { 1,2,3,4,5,6,7 };
	priority_queue<int, vector<int>> q(vec.begin(), vec.end());
	while (!q.empty()) {
		cout << q.top() << " ";
		q.pop();
	}
*/
	string s;
	s = to_string(4);

	cout << s << endl;
	cout << stoi(s) << endl;
	cin.get();
	return 0;
}
class Solution {
public:
	struct cmp{
		bool operator()(array<int, 2> a, array<int, 2> b) {
			return a[0] > b[0];
		}
	};
	int largestSumAfterKNegations(vector<int>& A, int K) {
		priority_queue<int, vector<array<int, 2>>, cmp> q;
		for (int i = 0; i < A.size(); i++) {
			if (A[i] < 0) {
				if (K > 0) {
					array<int, 2> a = { -A[i], i };
					q.push(a);
					K -= 1;
					A[i] = -A[i];
				}
				else {
					array<int, 2> buff = q.top();
					if (buff[0] < -A[i]) {
						A[buff[1]] = -buff[0];
						q.pop();
						q.push(array<int, 2>{ -A[i], i });
						A[i] = -A[i];
					}
				}
			}
		}
		int ret = 0;
		int min_num = A[0];
		
		for (auto num : A) {
			ret += num;
			min_num = min(min_num, num);
		}
		if (K % 2 == 1) {
			return ret - 2 * min_num;
		}
		return ret;
	}
};