#include <iostream>
using namespace std;

template<typename T> class MyClass;
template<typename T> void f_run(MyClass<T> a);
template<typename T> class F_class;


template <typename T>
class MyClass
{
public:
	MyClass(T a) :t(a){};
	void run(){
		cout << "run" << endl;
	}

	friend void friend_run(MyClass<T> a){
		cout << "friend_run" << endl;
		cout << a.data << endl;
	}
	friend void f_run<T>(MyClass<T> a);
	friend class F_class<T>;
private:
	int data=3;
	T t;
};
template<typename T>
void f_run(MyClass<T> a){
		cout << "f_run" << endl;
		cout << a.data << endl;
}
template<typename T>
class F_class
{
public:
	void run(MyClass<T> a){
		cout << a.t << endl;
	}
};

int main(){
	MyClass<int> mc(2);
	friend_run(mc);
	f_run(mc);
	F_class<int> fc;
	fc.run(mc);
	char* p = new char[1024];
	MyClass<int>* c = new(p) MyClass<int>(3);
	cin.get();
	return  0;
}