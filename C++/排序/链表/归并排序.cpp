#include "Node.h"
#include "utils.cpp"
template <typename T>
void merge_sort(Node<T>* start, Node<T>* end) {
	if (start == end) {
		return;
	}
	int length = get_length(start, end->next);
	Node<T>* mid = start;
	for (int i = 1; i < length / 2; i++) {
		mid = mid->next;
	}
	merge_sort(start, mid);
	merge_sort(mid->next, end);
	Node<T>* temp = new Node<T>();
	Node<T>* cursor_of_temp = temp;
	Node<T>* cursor_of_left = start;
	Node<T>* cursor_of_right = mid->next;
	while (cursor_of_left!= mid->next && cursor_of_right != end->next) {
		if (cursor_of_left->val <= cursor_of_right->val) {
			cursor_of_temp->next = new Node<T>(cursor_of_left->val);
			cursor_of_left = cursor_of_left->next;
		}
		else {
			cursor_of_temp->next = new Node<T>(cursor_of_right->val);
			cursor_of_right= cursor_of_right->next;
		}
		cursor_of_temp = cursor_of_temp->next;
	}
	while (cursor_of_left != mid->next) {
		cursor_of_temp->next = new Node<T>(cursor_of_left->val);
		cursor_of_temp = cursor_of_temp->next;
		cursor_of_left = cursor_of_left->next;
	}
	while (cursor_of_right != end->next) {
		cursor_of_temp->next = new Node<T>(cursor_of_right->val);
		cursor_of_right= cursor_of_right->next;
		cursor_of_temp = cursor_of_temp->next;
	}
	while (start != end->next) {
		start->val = temp->next->val;
		start = start->next;
		temp = temp->next;
	}
}
void test_merge_sort() {
	vector<int> a = { 1,2,3,4,5,8,6,3,3,54,6,8,4,2,2,2,3,344 };
	Node<int>* head = generate_linked_list(a);
	merge_sort(head, get_last_node(head));
	print_linked_list(head);
}
int main() { test_merge_sort(); }