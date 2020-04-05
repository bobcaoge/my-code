#include <iostream>
#include<vector>
using namespace std;
template<typename T>
void selection_sort(vector<T> &nums) {
	for (int i = 0; i < nums.size(); i++) {
		int flag = i;
		for (int j = i + 1; j < nums.size(); j++) {
			if ( nums[j] < nums[flag]) {
				flag = j;
			}
		}
		swap(nums[flag], nums[i]);
	}
}
void test_selection_sort() {
	vector<int> nums = { 1,4,7,89,4,2,5,8,9,5,4,2,2,4,67,9,9,3,4,5,7,4,3,23,3,45,5,6,7,7,8 };
	selection_sort(nums);
	for (auto num : nums) {
		cout << num << " ";
	}
	cout << endl;
}
//int main() { test_selection_sort(); }