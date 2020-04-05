#include "Node.h"
#include "utils.cpp"
template <typename T>
void selection_sort(Node<T>* head) {
	int length = get_length(head);
	for (int i = 0; i < length; i++) {
		Node<T>* cursor = head;
		for (int j = i; j < length; j++) {
			if (cursor->next != nullptr && cursor->val > cursor->next->val) {
				swap(cursor->val, cursor->next->val);
			}
			cursor = cursor->next;
		}
	}
}
void test_selection_sort() {
	vector<int> a = { 1,2,3,4,5,8,6,3,3,54,6,8,4,2,2,2,3,344 };
	Node<int>* head = generate_linked_list(a);
	selection_sort(head);
	print_linked_list(head);
}
//int main() { test_selection_sort(); }