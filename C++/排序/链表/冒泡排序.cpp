#include <iostream>
#include "Node.h"
#include "Node.cpp"
#include "utils.cpp"
using namespace std;

template<typename T>
void bubble_sort(Node<T>* head) {
	int length = 0;
	Node<T>* temp = head;
	while (temp != nullptr) {
		length++;
		temp = temp->next;
	}
	for (int i = 0; i < length-1; i++) {
		temp = head;
		for (int j = 0; j < length - i; j++) {
			if (temp->next != nullptr && temp->val > temp->next->val) {
				swap(temp->val, temp->next->val);
			}
			temp = temp->next;
		}
	}
}
void test_bubble_sort() {
	vector<int> a = { 1,2,3,4,5,8,6,3,3,54,6,8,4,2,2,2,3,344 };
	Node<int>* head = generate_linked_list(a);
	bubble_sort(head);
	print_linked_list(head);
}
//int main() { test_bubble_sort(); }
