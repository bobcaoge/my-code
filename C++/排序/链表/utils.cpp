#include <iostream>
#include "Node.h"
#include "Node.cpp"
#include <vector>
using namespace std;

template<typename T>
void print_linked_list(Node<T>* head, Node<T>* tail=nullptr) {
	while (head != tail) {
		cout << head->val<<" ";
		head = head->next;
	}
	cout << endl;
}
template<typename T>
Node<T>* generate_linked_list(vector<T> &values){
	Node<T>* head = new Node<T>(T());
	Node<T>* cursor = head;
	for (auto val : values) {
		cursor->next = new Node<T>(val);
		cursor = cursor->next;
	}
	return head->next;
}
template<typename T>
int get_length(Node<T>* head, Node<T>* tail=nullptr) {
	int length = 0;
	while (head != tail) {
		length++;
		head = head->next;
	}
	return length;
}
template<typename T>
Node<T>* get_last_node(Node<T>* head) {
	while (head != nullptr && head->next != nullptr) {
		head = head->next;
	}
	return head;
}