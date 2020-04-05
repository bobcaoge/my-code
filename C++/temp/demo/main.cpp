#include <iostream>
using namespace std;
class AAA
{

public:
	int a;
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
int &mymax(int &x, int &y){
	return x > y ? x : y;
}
int main1(){
	/*
	AAA* b = new AAA[10];
	cout << typeid(b).name() << endl;
	cout << sizeof(b) << endl;
	*/
	/*
	int length(100), i = 11;
	for (int i = 0; i < ~((int)0); i++);
	cout << length << endl;
	cout << i << endl;
	*/
	/*
	int x = 55, y = 77;
	mymax(x, y) += 12 + 11;
	cout << x << endl;
	cout << y << endl;
	*/
	int temp = 0;
	cin >> temp;
	int const a = temp;
	cin.get();
	return 0;
}
void hanoi(int n, string cur, string mid, string target) {
	if (n == 0) return;
	hanoi(n - 1, cur, target, mid);
	cout << "move "<<n<<" from " << cur.c_str() << " to " << target.c_str() << endl;
	hanoi(n - 1, mid, cur, target);
}

int main()
{
	hanoi(3, "left", "mid", "right");
	cin.get();
	return 0;
}







