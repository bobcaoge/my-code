#pragma once
#include "Node.h"
class Linkedlist
{
	template<class T>
	class Node
	{
	public:
		T value;
		Node* next;
	public:
		Node() {}
		Node(T value)
		{
			this->value = value;
		}

		~Node() {}
	};

public:
	template<class T>Node* head;
public:
	Linkedlist();
	template<class T>bool is_empty();
	template<class T>Node* insertFromHead(Node* head, T value);
	template<class T>Node* insertToEnd(Node* head, T value);
	template<class T>bool remove(Node* head, T value);
	template<class T>bool remove(Node* head, int index);
	template<class T>bool find(Node* head, T value);

	~Linkedlist();
};
Linkedlist::Linkedlist()
{
}
Linkedlist::~Linkedlist()
{
}
template<class T>bool Linkedlist::is_empty()
{
	return (head == nullptr);
}
template<class T>Node* Linkedlist::insertFromHead(Node* head, T value)
{
	Node* new_node = new Node(value);
	if (is_empty) {
		head = new_node;
		return head;
	}
	value->next = head;
	head = new_node;
	return head;
}
template<class T>Node* Linkedlist::insertToEnd(Node* head, T value)
{
	Node * new_node = new Node(value);
	if (head == nullptr) {
		head = new_node;
		return head;
	}
	Node* cur = head;
	while (cur->next != nullptr) {
		cur = cur->next;
	}
	cur->next = new_node;
	return head;
}
template<class T>bool Linkedlist::remove(Node* head, T value)
{
	return false;
}
template<class T>bool Linkedlist::remove(Node* head, int index)
{
	return false;
}
template<class T>bool Linkedlist::find(Node* head, T value)
{
	return false;
}

