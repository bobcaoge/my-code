#pragma once
#ifndef SINGLELINK_H
#define SINGLELINK_H
#include<vector>

using namespace std;

/*结点定义*/
template<typename T>
class Node {
public:
	T value;//值
	Node<T>*next;//指针
public:
	Node() = default;
	Node(T _value, Node<T>*_next) :value(_value), next(_next) {}
};


/*链表定义（接口）*/
template<typename T>
class SingleLink {
private:
	Node<T>*head;
	int count;
public:
	SingleLink();//构造函数（生成空表）
	void add_front(T value);
	void add_last(int index, T value);
	void add(int index, T value);
	void del_index(int index);
	void del_value(T VALUE);
	void show();
	Node<T>*find_index(int index);
	vector<int>*find_value(T value);
	int find_value_aid(T VALUE);
	//链表操作函数声明


};


/*构造函数*/
template<typename T>
SingleLink<T>::SingleLink() {
	head = new Node<T>(0, nullptr);
	/*head->value = 0;
	head->next = nullptr;*/
	count = 0;
}


/*插入*/
//最前面插入值为value的结点
template<typename T>
void SingleLink<T>::add_front(T value) {
	Node<T>* node = new Node<T>(value, head->next);
	head->next = node;
	count++;
	return;
}
//下标index的结点后插入值为value的结点(index=count-1)
template<typename T>
void SingleLink<T>::add(int index, T value) {
	if (index < 0 || index >= count) return;
	Node<T>*index_node = find_index(index);//注意是在index结点后插入，如果是index结点前插入需要find(index-1)操作需要改变
	Node<T>*node = new Node<T>(value, index_node->next);
	index_node->next = node;
	count++;
	return;
}
//最后面插入值为value的结点
template<typename T>
void SingleLink<T>::add_last(int index, T value) {
	add(index, value);
	return;
}

/*查找*/
//查找下标为index的结点并返回指向该结点指针
template<typename T>
Node<T>*SingleLink<T>::find_index(int index) {
	//cout << count << endl;
	//cout << (index < 0) << " =====" << (index >= count)<<index<<" "<<count << endl;
	if (index < 0 || index >= count) return nullptr;
	Node<T>*node = head->next;
	while (index) {
		node = node->next;
		index--;
	}
	return node;
}
//查找值为VALUE的结点并返回结点的index向量指针
template<typename T>
vector<int>* SingleLink<T>::find_value(T VALUE) {
	vector<int> *VECTOR = new vector<int>();
	Node<T>*node = head->next;
	int index = 0;
	int num = 0;
	while (node != nullptr) {
		if (node->value = VALUE) {
			VECTOR->push_back(index);
			num++;
		};
		node = node->next;
		index++;
	}
	return VECTOR;
}

//查找值为VALUE的结点并返回结点个数
template<typename T>
int SingleLink<T>::find_value_aid(T VALUE) {
	vector<int> VECTOR;
	Node<T>*node = head->next;
	int index = 0;
	int num = 0;
	while (node != nullptr) {
		if (node->value = VALUE) {
			VECTOR.push_back(index);
			num++;
		};
		node = node->next;
		index++;
	}
	return num;
}

/*输出列表的value*/
//顺序输出列表值并输出结点个数
template<typename T>
void SingleLink<T>::show() {
	Node<T>*node = head->next;
	while (node != nullptr) {
		cout << node->value << "  ";
		node = node->next;
	}
	cout << endl << count << endl;
	return;
}

/*删除*/
//删除下标为index的结点
template<typename T>
void SingleLink<T>::del_index(int index) {

	if (index < 0 || index >= count) return;
	if (index = 0) {
		head->next = head->next->next;
		delete head->next;
		head->next = nullptr;
		return;
	}
	Node<T>*node = find_index(index);//找到下标为index的结点
	cout << index << endl;
	Node<T>*node_front = find_index(index - 1);//找到下标为index-1的结点
	node_front->next = node->next;//将index-1结点的指针指向index->next
	delete node;
	node = nullptr;
	count--;
	return;

}

//删除值为value的结点（可能不止一个节点的值为VALUE）
template <typename T>
void SingleLink<T>::del_value(T VALUE) {
	vector<int>*p = find_value(VALUE);
	int num = find_value_aid(VALUE);
	//vector<int>node_index;

	for (int i = 0; i < num; i++) {
		int temp = (*p)[i];
		del_index(temp);
	}
	return;
}

#endif

