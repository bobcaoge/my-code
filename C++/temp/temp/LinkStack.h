#pragma once
#ifndef LINKSTACK_H
#define LINKSTACK_H

/*����ڵ�ṹ*/
template <typename T>
class Node {
public:
	T value;
	Node<T>*next;
public:
	Node() = default;
	Node(T _value, Node<T>* _next) :value(_value), next(_next) {};
	Node(T _value) {
		value = _value;
		next = nullptr;
	}
	Node() {
		next = nullptr;
	}
};



/*ջ�ĳ������ݽṹ*/
template <typename T>
class LinkStack
{
public:
	LinkStack();	//�������캯����Ĭ�ϵ�ջ����Ϊ10
	T top();		//��ȡջ��Ԫ��
	void push(T t);		//ѹջ����
	T pop();		//��ջ����
	bool isEmpty();		//�пղ���
	int size();
private:
	int count;			//ջ��Ԫ������
	Node<T>* head;			//�ײ�Ϊ����
};


/*���캯��������ֻ����һ���յ�ͷ���Ŀ�ջ��*/
template<typename T>
LinkStack<T>::LinkStack() {
	head = new Node<T>(0, NULL);
	/*head->value = 0;
	head->next = nullptr;*/
	count = 0;
}



/*����ջ�Ĵ�С*/
template <typename T>
int LinkStack<T>::size()
{
	return count;
};



/*ջ���пղ���*/
template <typename T>
bool LinkStack<T>::isEmpty()
{
	return count == 0;
};



/*����Ԫ��(ʼ����head������룩*/
template<typename T>
void LinkStack<T>::push(T VALUE)
{
	Node <T> *node = new  Node<T>(VALUE, head->next);
	head->next = node;
	count++;
};


/*��ջ*/
template <typename T>
T LinkStack<T>::pop()
{
	if (head->next != nullptr) //ջ���ж�
	{
		Node<T>* node = head->next;//ջ��Ҫ�����Ľ��
		head->next = node->next;
		T value = node->value;
		delete node;
		node = nullptr;
		count--;
		return value;
	}
	else return nullptr;
};



/*��ȡջ��Ԫ��*/
template <typename T>
T LinkStack<T>::top()
{
	if (head->next != nullptr)
		return head->next->value;
	else return nullptr;
};



#endif


