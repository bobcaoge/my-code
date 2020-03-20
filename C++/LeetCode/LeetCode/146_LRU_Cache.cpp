#include <iostream>
#include <unordered_map>
using namespace std;
class Node {
public:
	int data;
	int value;
	Node* pre;
	Node* next;
	Node(int d, int v) {
		value = v;
		data = d;
		pre = NULL;
		next = NULL;
	}
};
void remove(Node* node) {
	Node* pre = node->pre;
	Node* next = node->next;
	pre->next = next;
	next->pre = pre;
}
void add(Node* tail, Node* node) {
	tail->pre->next = node;
	node->next = tail;
	node->pre = tail->pre;
	tail->pre = node;
}
class LRUCache {
public:
	int size;
	int length;
	Node* pre;
	Node* next;
	unordered_map<int, Node*> m;
	LRUCache(int capacity) {
		length = 0;
		size = capacity;
		pre = new Node(0, 0);
		next = new Node(0, 0);
		pre->next = next;
		next->pre = pre;
	}

	int get(int key) {
		if (m.find(key) != m.end()) {
			remove(m[key]);
			add(next, m[key]);
			return m[key]->value;
		}
		return -1;
	}

	void put(int key, int value) {
		if (m.find(key) != m.end()) {
			remove(m[key]);
			add(next, m[key]);
			m[key]->value = value;
		}
		else {
			m[key] = new Node(key, value);
			add(next,m[key]);
			length++;
			if (length > size) {
				m.erase(m.find(pre->next->data));
				remove(pre->next);
				length--;
			}
		}
	}
};

int main_LRU() {
	LRUCache* obj = new LRUCache(2);
	int param_1 = obj->get(3);
	obj->put(1, 1);
	obj->put(2, 2);
	cout << obj->get(1) << endl;
	obj->put(3, 3);
	cout << obj->get(2) << endl;
	cin.get();
	return 0;
}
