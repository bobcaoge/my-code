#pragma once
#ifndef SINGLELINK_H
#define SINGLELINK_H
#include<vector>

using namespace std;

/*��㶨��*/
template<typename T>
class Node {
public:
	T value;//ֵ
	Node<T>*next;//ָ��
public:
	Node() = default;
	Node(T _value, Node<T>*_next) :value(_value), next(_next) {}
};


/*�����壨�ӿڣ�*/
template<typename T>
class SingleLink {
private:
	Node<T>*head;
	int count;
public:
	SingleLink();//���캯�������ɿձ�
	void add_front(T value);
	void add_last(int index, T value);
	void add(int index, T value);
	void del_index(int index);
	void del_value(T VALUE);
	void show();
	Node<T>*find_index(int index);
	vector<int>*find_value(T value);
	int find_value_aid(T VALUE);
	//���������������


};


/*���캯��*/
template<typename T>
SingleLink<T>::SingleLink() {
	head = new Node<T>(0, nullptr);
	/*head->value = 0;
	head->next = nullptr;*/
	count = 0;
}


/*����*/
//��ǰ�����ֵΪvalue�Ľ��
template<typename T>
void SingleLink<T>::add_front(T value) {
	Node<T>* node = new Node<T>(value, head->next);
	head->next = node;
	count++;
	return;
}
//�±�index�Ľ������ֵΪvalue�Ľ��(index=count-1)
template<typename T>
void SingleLink<T>::add(int index, T value) {
	if (index < 0 || index >= count) return;
	Node<T>*index_node = find_index(index);//ע������index������룬�����index���ǰ������Ҫfind(index-1)������Ҫ�ı�
	Node<T>*node = new Node<T>(value, index_node->next);
	index_node->next = node;
	count++;
	return;
}
//��������ֵΪvalue�Ľ��
template<typename T>
void SingleLink<T>::add_last(int index, T value) {
	add(index, value);
	return;
}

/*����*/
//�����±�Ϊindex�Ľ�㲢����ָ��ý��ָ��
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
//����ֵΪVALUE�Ľ�㲢���ؽ���index����ָ��
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

//����ֵΪVALUE�Ľ�㲢���ؽ�����
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

/*����б��value*/
//˳������б�ֵ�����������
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

/*ɾ��*/
//ɾ���±�Ϊindex�Ľ��
template<typename T>
void SingleLink<T>::del_index(int index) {

	if (index < 0 || index >= count) return;
	if (index = 0) {
		head->next = head->next->next;
		delete head->next;
		head->next = nullptr;
		return;
	}
	Node<T>*node = find_index(index);//�ҵ��±�Ϊindex�Ľ��
	cout << index << endl;
	Node<T>*node_front = find_index(index - 1);//�ҵ��±�Ϊindex-1�Ľ��
	node_front->next = node->next;//��index-1����ָ��ָ��index->next
	delete node;
	node = nullptr;
	count--;
	return;

}

//ɾ��ֵΪvalue�Ľ�㣨���ܲ�ֹһ���ڵ��ֵΪVALUE��
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

