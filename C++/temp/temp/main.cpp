#include<iostream>
#include "LinkStack.h"
using namespace std;
class Base {
public:
	static int num;
	Base() {
		num++;
	}
	void show_num() {
		cout << num << endl;
	}
};
int Base::num = 0;
class SubBase: public Base {

};

int main()
{
	Base b;
	b.show_num();
	SubBase sub;
	sub.show_num();


	getchar();
	return 0;
}
