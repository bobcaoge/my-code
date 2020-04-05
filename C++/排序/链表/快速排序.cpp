#include "Node.h"
#include "utils.cpp"
template <typename T>
void quick_sort(Node<T>* start, Node<T>* end, int length) {
	if (length <= 1) {
		return;
	}
	//print_linked_list(start, end->next);
	T pivot = end->val;
	int length_lt_pivot = 0;
	Node<T>* node_before_pivot = nullptr;
	Node<T>* node_lt_pivot = start; //用于记录小于标志位的边界
	Node<T>* cursor = start;
	//cout << (cursor == nullptr)<<" "<<(start == nullptr) << endl;
	while (cursor != end) {
		if (cursor->val < pivot) {
			swap(node_lt_pivot->val, cursor->val);
			node_before_pivot = node_lt_pivot;
			node_lt_pivot = node_lt_pivot->next;
			length_lt_pivot++;
		}
		cursor = cursor->next;
		
	}
	swap(node_lt_pivot->val, end->val);
	quick_sort(start, node_before_pivot, length_lt_pivot);
	quick_sort(node_lt_pivot->next, end, length-length_lt_pivot-1);
}
void test_quick_sort() {
	vector<int> a = { 1,2,3,4,5,8,6,3,3,54,6,8,4,2,2,2,3,344 };
	//vector<int> a = { 4,5,9,6,1,3,7,8,2,10 };
	Node<int>* head = generate_linked_list(a);
	quick_sort(head, get_last_node(head),get_length(head));
	print_linked_list(head);
}
//int main() { test_quick_sort(); }