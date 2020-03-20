#include <iostream>
using namespace std;



class MyCircularDeque {
public:
	int* nums;
	int front;
	int back;
	int size;
	int length;
	/** Initialize your data structure here. Set the size of the deque to be k. */
	MyCircularDeque(int k) {
		size = k;
		nums = new int[k];
		front = -1;
		back = -1;
		length = 0;
	}

	/** Adds an item at the front of Deque. Return true if the operation is successful. */
	bool insertFront(int value) {
		if (!isFull()) {
			if (isEmpty()) {
				front = 0;
				nums[front] = value;
				back = (front+1) % size;
			}
			else {
				front = (front - 1 + size) % size;
				nums[front] = value;
			}
			length++;
			return true;
		}
		return false;
	}

	/** Adds an item at the rear of Deque. Return true if the operation is successful. */
	bool insertLast(int value) {
		if (!isFull()) {
			if (front == -1) {
				front = 0;
				nums[front] = value;
				back = (front+1) % size;
			}
			else {
				nums[back] = value;
				back = (back + 1 ) % size;
			}
			length++;
			return true;
		}
		return false;
	}



	/** Deletes an item from the front of Deque. Return true if the operation is successful. */
	bool deleteFront() {
		if (!isEmpty()) {
			length--;
			if (isEmpty()) {
				front = back = -1;
			}else{
				front = (front + 1) % size;
			}
			return true;
		}
		return false;

	}

	/** Deletes an item from the rear of Deque. Return true if the operation is successful. */
	bool deleteLast() {
		if (!isEmpty()) {
			length--;
			if (isEmpty()) {
				front = back = -1;
			}else{
				back = (back - 1+size) % size;
			}
			return true;
		}
		return false;


	}

	/** Get the front item from the deque. */
	int getFront() {
		if (!isEmpty()) {
			return nums[front];
		}
		return -1;

	}

	/** Get the last item from the deque. */
	int getRear() {

		if (!isEmpty()) {
			return nums[(back-1+size)%size];
		}
		return -1;
	}

	/** Checks whether the circular deque is empty or not. */
	bool isEmpty() {
		return length == 0;

	}

	/** Checks whether the circular deque is full or not. */
	bool isFull() {
		return length == size;
	}
};

void print_queue(MyCircularDeque cd) {
	if (cd.isEmpty()) {
		cout << "empty" << endl;
		return;
	}
	
	for (int i=0;i<cd.length ;i++ ) {
		cout << cd.nums[(cd.front + i) % cd.size]<<" ";
	}
	cout << endl;
}
int main() {
	MyCircularDeque cd(10);
	for (int i = 0; i < 9; i++) {
		cd.insertFront(i + 8);
		//print_queue(cd);
		cd.insertLast(i + 8);
		//print_queue(cd);
		/*cout << "cd.front   cd.back " << cd.front << " " << cd.back << endl;
		cout << "length: " << cd.length << endl;
		cout <<"isEmpty: "<< cd.isEmpty() << endl;
		cout <<"isFull: "<< cd.isFull() << endl;
		cout <<"front and last: "<< cd.getFront() << " " << cd.getRear() << endl;
		cout << endl;
		*/
	}
	for (int i = 0; i < 11; i++) {
		print_queue(cd);
		cout << cd.deleteFront() << endl;
		cout << "cd.front   cd.back " << cd.front << " " << cd.back << endl;
		cout <<"front and last: "<< cd.getFront() << " " << cd.getRear() << endl;
		cout << cd.deleteLast() << endl;
		cout << "cd.front   cd.back " << cd.front << " " << cd.back << endl;
		cout <<"front and last: "<< cd.getFront() << " " << cd.getRear() << endl;
		cout << endl;
	}
	
	cin.get();
	return 0;
}
