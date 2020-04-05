#include <iostream>
#include <vector>
using namespace std;
template<typename T>
void heap_push(vector<T> &nums, T num) {
	nums.push_back(num);
	int cur = nums.size() - 1;
	int parent =(cur + 1) / 2 - 1; 
	while (cur != 0 && nums[cur] > nums[parent]) {
		swap(nums[cur], nums[parent]);
		cur = parent;
		parent = (cur + 1) / 2 - 1;
	}
}
template<typename T>
void heap_verify(vector<T> &nums) {
	for (int i = 0; i < nums.size(); i++) {
		int cur = i;
		int parent =(cur + 1) / 2 - 1; 
		while (cur != 0 && nums[cur] > nums[parent]) {
			swap(nums[cur], nums[parent]);
			cur = parent;
			parent = (cur + 1) / 2 - 1;
		}
	}
}
template <typename T>
void sink(vector<T> &heap, int start, int end) {
	T cur = heap[start];
	int parent = start;
	int child = (parent + 1) * 2 - 1;
	while (child <= end) {
		if (child + 1 <= end && heap[child + 1] > heap[child]) child++;
		if (heap[child] <= cur) break;
		heap[parent] = heap[child];
		parent = child;
		child = (parent + 1) * 2 - 1;
	}
	heap[parent] = cur;
}
template<typename T>
T heap_pop(vector<T>& heap, int length) {
	T ret = heap[0];
	length--;
	int cur= heap[length];
	int parent, child;
	for (parent = 0; parent * 2 < length; parent = child) {
		child = (parent + 1) * 2 - 1;
		if (child +1 < length && heap[child+1]> heap[child]) {
			child++;
		}
		if (heap[child] <= cur) break;
		heap[parent] = heap[child];
	}
	heap[parent] = cur;

	return ret;
}
template<typename T>
bool valid_heap(vector<T>& heap, int length) {
	for (int i = 0; i < length; i++) {
		int left = (i + 1) * 2 - 1;
		int right = left + 1;
		if (left < length && heap[i] < heap[left]) return false;
		if (right< length && heap[i] < heap[right]) return false;
	}
	return true;
}
template<typename T>
void print(vector<T> & nums) {
	for (auto num : nums) {
		cout << num << " ";
	}
	cout << endl;
}
template <typename T>
void heap_sort(vector<T>& nums) {
	for (int i = 0; i < nums.size(); i++) {
		sink(nums, nums.size() - i - 1, nums.size()-1);
	}
	for (int i = 0; i < nums.size() - 1; i++) {
		swap(nums[0], nums[nums.size() - i - 1]);
		sink(nums, 0, nums.size() - i - 2);
	}
}
template <typename T>
void heap_sort_1(vector<T>& nums) {
	heap_verify(nums);
	for (int i = nums.size() - 1; i >= 0; i--) {
		//if (!valid_heap(nums, i + 1)) {
		//	cout << i + 1 << endl;;
		//	break;
		//}
		nums[i] = heap_pop(nums, i+1);
		//print(nums);
	}
}

void test_heap_sort() {
	vector<int> nums = { 1,4,7,89,4,2,5,8,9,5,4,2,2,4,67,9,9,3,4,5,7,4,3,23,3,45,5,6,7,7,8 };
//	vector<int> nums = {1,3,3,4,5,5,5,5,6,67,7 };
	heap_sort(nums);
	for (auto num : nums) {
		cout << num << " ";
	}
	cout << endl;
}
int main() { test_heap_sort(); }