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
// ���Է�����ʱ����
class A {
public:
	int a;
	A(int b) :a(b) {};
};
A get(int a) {
	A ret(a);
	return ret;
}
//����ʹ�ú����ڲ����� ����ջ�е���ʱ���������ᱻ����
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
	//��Ԫ������ģ���ڲ�ʵ��
	friend void print(complex t) {
		cout << t.t << endl;
	}*/
	// ��Դ������ģ���ⲿʵ��
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
class AAA
{
public:
	virtual void fun1(){
		cout << "fun1 A" << endl;
	}
	void fun2(){
		cout << "fun2 A" << endl;
	}
};
class BBB :public AAA
{
private:
	void fun1(){
		cout << "fun1 B" << endl;
	}
	virtual void fun2(){
		cout << "fun2 B" << endl;
	}

};
int main(){
	AAA* a = new BBB();
	a->fun2();
	cin.get();
	return 0;
}

int mainaaaaa() {
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













