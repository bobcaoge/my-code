#include <iostream>
using namespace std;

template <typename T>
void merge_sort(T nums[], int start, int end) {
	if (end <= start) {
		return;
	}
	int mid = (start + end) / 2;
	merge_sort(nums, start, mid);
	merge_sort(nums, mid + 1, end);
	int i = start;
	int j = mid + 1;
	T* p = new T[end - start + 1];
	int k = 0;
	while (i <= mid && j <= end) {
		if (nums[i] <= nums[j]) {
			p[k++] = nums[i++];
		}
		else {
			p[k++] = nums[j++];
		}
	}
	while (i <= mid) p[k++] = nums[i++];
	while (j <= end) p[k++] = nums[j++];
	//for (int i = 0; i < k; i++)nums[start + i] = p[i];
	while (k > 0) nums[end--] = p[--k];
	delete p;
}
void test_merge_sort()
{
	int nums[] = { 0,3,5,2,7,9,5,4,2,2,4,56,8,4,67,898 };
	merge_sort(nums, 0, (sizeof(nums) / 4) - 1);
	for (auto num : nums) {
		cout << num << " ";
	}
	cout << endl;
}
//int main() { test(); }
