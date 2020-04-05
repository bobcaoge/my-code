#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
//快速排序选取索引end作为pivot，将所有小于pivot的放在左边，最后将pivot放在正确的位置，在排序两侧
template<typename T>
void print(T nums[], int start, int end) {
	for (int i = start; i <= end; i++) {
		cout << nums[i] << " ";
	}
	cout << endl;
}
template <typename T>
void quick_sort(T nums[], int start, int end) {
	if (start >= end) {
		return;
	}
	int pivot = nums[end];
	int mid = start;

	for (int i = start; i < end; i++) {
		if (nums[i] < pivot) {
			swap(nums[i], nums[mid]);
			mid++;
		}
	}
	swap(nums[end], nums[mid]);
	quick_sort(nums, start, mid-1);
	quick_sort(nums, mid + 1, end);
}
/*
void test()
{
	int nums[] = { 0,3,5,2,7,9,5,4,2,2,4,56,8,4,67,898 };
	quick_sort(nums, 0, (sizeof(nums)/4)-1);
	for (auto num : nums) {
		cout << num << " ";
	}
	cout << endl;
}*/
//int main() { test(); }