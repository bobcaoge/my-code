#pragma once
template<class T>
class Node
{
public:
	T value;
	Node* next;
public:
	Node();
	Node(T value)
	{
		this->value = value;
	}
	
	~Node();
};

