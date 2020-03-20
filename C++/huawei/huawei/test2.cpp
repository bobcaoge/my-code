#include<iostream>
using namespace std;
int main() {
	int m;
	int n;
	cin >> n >> m;
	long ret = 1;
	
	int to_mod = 1000000007;
	for (int i = m+1; i <= m + n - 1; i++) {
		ret = ret*i % to_mod;
	}
	for (int i = 2; i <= n - 1; i++) {
		ret /= i;
	}
	cout << ret;
	cin.get();
	cin.get();
	return 0;
}