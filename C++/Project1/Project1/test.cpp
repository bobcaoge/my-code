#include <iostream>
using namespace std;
struct Test
{
	int a;
	int b[5] = { 0 };
};
void change(Test t)
{
	t.b[2] = 100;
	cout << t.b[2] << endl;
}
int main111()
{
	Test t;
	t.a = 2;
	change(t);
	for each (int var in t.b)
	{
		cout << var << " ";
	}
	cout << endl;
	cin.get();
	return 0;
}
char a[100];
int main()
{

	int * b = new(a) int;
	cout << "b: " <<b << endl;
	//delete b;
	b = new(a) int;
	cout <<"b: "<< b << endl;
	cin.get();
	return 0;
}