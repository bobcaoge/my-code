#pragma once
template <class T>
class Node
{
public:
	T val;
	Node* next;
public:
	Node(T value) {
		val = value;
		next = nullptr;
	}
	Node() {
		next = nullptr;
	}
};

