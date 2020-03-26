#include <vector>
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
// 测试返回临时对象
class A {
public:
	int a;
	A(int b) :a(b) {};
};
A get(int a) {
	A ret(a);
	return ret;
}
//测试使用函数内部变量 函数栈中的临时对象用完后会被销毁
void add(vector<A> arr) {
	arr.push_back(A(3));
	cout << arr.size() << endl;
}
int mainA()
{
	vector<A> arr;
	add(arr);
	cout << arr.size() << endl;
	getchar();
	return 0;
}
template <class T> class complex;
template<class T> void print(complex<T> t);
template<class T> class B;

template<class T>
class complex
{
public:
	complex(T tt) : t(tt) {};
	/*
	//友元函数在模板内部实现
	friend void print(complex t) {
		cout << t.t << endl;
	}*/
	// 有源函数在模板外部实现
	friend void print<T>(complex<T> t);
	friend class B<T>;
private:
	T t;
	
};
template<class T>
class B
{
public:

	void print(complex<T> a) {
		cout << a.t << endl;
	}
};
template<class T>
void print(complex<T> t) {
	cout << t.t << endl;
}
class C
{
public:
	static int a;

};
int C::a = 0;

int main() {
	/*
	complex<int> a(3);
	print(a);*/

//complex<int> a(3);
//	B<int> b;
//	b.print(a);
	C c;
	c.a = 10;
	cout << c.a << endl;


	cin.get();
	return 0;
}













