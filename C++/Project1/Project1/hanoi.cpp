#include <iostream>
#include <stdlib.h>
#include <stack>
#include <array>
#include <stack>
#include <string>
using namespace std;
void hanoi(int n, char A, char B, char C, int* num) {
	if (n == 0) {
		return;
	}else {
		hanoi(n - 1, A, C, B, num);
		cout << A << "-->" << C << endl;
		*num += 1;
		hanoi(n - 1, B, A, C, num);
	}
}
enum Move{
	LToM, MToR, RToM, MToL,OTHER
};

int moveFromfstackTotStack(array<Move, 2>& record,Move pre,Move now,  stack<int> *from, stack<int> *to, string from_str, string to_str) {

	if (record[0] != pre && from->top() < to->top()) {
		to->push(from->top());
		from->pop();
		record[0] = now;
		cout << "move " << to->top() << " from " << from_str << " to " << to_str << endl;
		return 1;
	}
	return 0;
	
}
int moveFromfstackTotStack2(Move& record,Move pre,Move now,  stack<int> &from, stack<int> &to, string from_str, string to_str) {

	if (record != pre && from.top() < to.top()) {
		to.push(from.top());
		from.pop();
		record = now;
		cout << "move " << to.top() << " from " << from_str << " to " << to_str << endl;
		return 1;
	}
	return 0;
	
}
void hanoiwithstack(int n) {
	//³õÊ¼»¯Õ»
	/*stack<int> *left = new stack<int>;
	left->push(INT_MAX);
	for (int i = n; i > 0; i--) {
		left->push(i);
	}
	stack<int>* mid = new stack<int>;
	mid->push(INT_MAX);
	stack<int>* right = new stack<int>;
	right->push(INT_MAX);
*/
	stack<int> left;
	left.push(INT_MAX);
	for (int i = n; i > 0; i--) {
		left.push(i);
	}
	stack<int> mid;
	mid.push(INT_MAX);
	stack<int> right;
	right.push(INT_MAX);
	
	int count = 0;
	//array<Move, 2>* record = new array<Move, 2>{ Move::OTHER };
	//array<Move, 2> record ={ Move::OTHER };

	Move record = Move::OTHER;
	while (right.size()<n+1 ) {
		count += moveFromfstackTotStack2(record, Move::LToM, Move::MToL, mid, left, "mid", "left");
		count += moveFromfstackTotStack2(record, Move::MToL, Move::LToM, left, mid, "left", "mid");
		count += moveFromfstackTotStack2(record, Move::MToR, Move::RToM, right, mid, "right", "mid");
		count += moveFromfstackTotStack2(record, Move::RToM, Move::MToR, mid, right, "mid", "right");

	}
	cout << count << endl;


}

void change(Move& a) {
	a = Move::LToM;

}
/*int main() {
	/*int * a = new int(0);
	hanoi(3, 'A', 'B', 'C', a);
	cout << *a << endl;
	hanoiwithstack(3);
	Move a = Move::OTHER;
	change(a);
	//cout << a << endl;
	system("pause");
	return 0;
}
	*/