#include "Node.h"
#include "utils.cpp"
template <typename T>
void insertion_sort(Node<T>* head) {
	int length = get_length(head);

	Node<T>* cur = head;
	for (int i = 0; i < length; i++) {
		Node<T>* cursor = head;
		while (cur != cursor && cur->val >= cursor->val) cursor = cursor->next;
		T last = cur->val;
		while (cursor != cur->next) {
			T temp = cursor->val;
			cursor->val = last;
			last = temp;
			cursor = cursor->next;
		}
		cur = cur->next;
	}
}
void test_insertion_sort() {
	vector<int> a = { 1,2,3,4,5,8,6,3,3,54,6,8,4,2,2,2,3,344 };
	Node<int>* head = generate_linked_list(a);
	insertion_sort(head);
	print_linked_list(head);
}
//int main() { test_insertion_sort(); }