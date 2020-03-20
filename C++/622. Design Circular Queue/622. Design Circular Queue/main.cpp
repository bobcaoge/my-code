class MyCircularQueue {
public:
	int front;
	int rear;
	int size;
	int length;
	int* nums;
	/** Initialize your data structure here. Set the size of the queue to be k. */
	MyCircularQueue(int k) {
		nums = new int[k];
		size = k;
		length = 0;
		front = 0;
		rear = 0;
	}

	/** Insert an element into the circular queue. Return true if the operation is successful. */
	bool enQueue(int value) {
		if (!isFull()) {
			if (isEmpty()) {
				nums[front] = value;
			}else{
				rear = (rear + 1) % size;
				nums[rear] = value;
			}
			length++;
			return true;
		}
		return false;

	}

	/** Delete an element from the circular queue. Return true if the operation is successful. */
	bool deQueue() {
		if (isEmpty()) {
			return false;
		}
		front = (front + 1) % size;
		length--;
		if (isEmpty()) {
			front = rear = 0;
		}
		return true;
	}

	/** Get the front item from the queue. */
	int Front() {
		if (isEmpty()) {
			return -1;
		}
		return nums[front];

	}

	/** Get the last item from the queue. */
	int Rear() {
		if (isEmpty()) {
			return -1;
		}
		return nums[rear];

	}

	/** Checks whether the circular queue is empty or not. */
	bool isEmpty() {
		return length == 0;

	}

	/** Checks whether the circular queue is full or not. */
	bool isFull() {
		return length == size;

	}
};
