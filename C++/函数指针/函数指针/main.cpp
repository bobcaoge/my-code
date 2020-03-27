#include <iostream>
using namespace std;
int add(int a, int b){
	return a + b;
}
int jian(int a, int b){
	return a - b;
}
class Base
{
public:
	int add(int a, int b){
		return a + b;
	}
	int jian(int a, int b){
		return a - b;
	}
};
int main(){
	/*
	int(*p)(int, int) = add;
	int(*pp[2])(int, int) = { add, jian };
	for (auto fun : pp){
		cout << fun(2, 3) << endl;
	}
	//cout << p(2, 3) << endl;
*/
	Base base;
	int(Base::*pp)(int, int) = &Base::add;
	cout << (base.*pp)(1, 3);
	int(Base::*p[2])(int, int) = { &Base::add, &Base::jian };
	cout << "=======" << endl;

	for (auto fun:p){
		cout << (base.*fun)(2, 3) << endl;
	}
	cin.get();
	return 0;
}