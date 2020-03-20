#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
bool cmp(vector<int> a, vector<int> b) {
	if (a.size() >= b.size()) {
		return true;
	}
	return false;
}
int main3() {
	//对基础类型进行排序
	/*
	vector<int> arr;
	arr.push_back(1);
	arr.push_back(3);
	arr.push_back(2);
	arr.push_back(10);
	arr.push_back(-1);

	for (auto it = arr.begin(); it != arr.end(); it++) {
		cout << *it << " ";
	}

	cout << endl;
	sort(arr.begin(), arr.end());
	for (auto it = arr.begin(); it != arr.end(); it++) {
		cout << *it << " ";
	}
*/
	//对较为复杂类型对象进行排序

	vector<vector<int>> arr;
	arr.push_back({ 1,1,1,1 });
	arr.push_back({ 2,2,2 });
	arr.push_back({ 3,3 });
	arr.push_back({ 4 });
	stable_sort(arr.begin(), arr.end(), cmp);
	for (vector<int> temp : arr) {
		for (int num : temp) {
			cout << num << " ";
		}
		cout << endl;
	}
	cin.get();
	return 0;
}
