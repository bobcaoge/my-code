#include <iostream>
using namespace std;


class Node {
public :
	int value;
	Node* next;
	Node(int value) {
		this->value = value;
	}
};
Node* create(int value) {
	int cur = 0;
	Node* head = NULL;
	Node* ret = NULL;
	while (value != 0) {
		cur = value % 10;
		value = value / 10;
		if (ret == NULL) {
			ret = new Node(cur);
			head = ret;

		}
		else {
			ret->next = new Node(cur);
			ret = ret->next;
		}
	}
	
	return head;
}
Node* add(Node* first, Node* second) {
	if (first == NULL) {
		return second;
	}
	if (second == NULL) {
		return first;
	}

	int carry = 0;
	int cur = 0;
	int value_of_first = 0;
	int value_of_second = 0;
	Node* head = NULL;
	Node* cursor = NULL;
	Node* next_node = NULL;
	while (first != NULL || second != NULL) {
		if (first != NULL) {
			value_of_first = first->value;
			first = first->next;
		}
		else {
			value_of_first = 0;
		}
		if (second != NULL) {
			value_of_second = second->value;
			second = second->next;
		}
		else {
			value_of_second = 0;
		}
		cur = value_of_first + value_of_second + carry;
		next_node = new Node(cur % 10);
		carry = cur / 10;
		if (head == NULL) {
			head = next_node;
			cursor = next_node;
		}
		else {
			cursor->next = next_node;
			cursor = cursor->next;
		}
	}
	if (carry != 0) {
		cursor->next = new Node(carry);
	}
	return head;
}
void print_linkedlist(Node* head) {
	while (head != NULL) {
		cout << head->value << " " ;
		head = head->next;
	}
	cout << endl;
}
int main() {
	Node* first = create(342);
	print_linkedlist(first);
	Node* second = create(1234567999);
	print_linkedlist(second);
	Node* result = add(first, second);
	print_linkedlist(result);
	cin.get();
	return 0;
}