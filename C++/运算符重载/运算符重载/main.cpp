#include <iostream>
#include "Pointer.h"
#include <stdlib.h>
using std::cout;
using std::cin;
using std::endl;

int main1()
{
	Pointer p1(2, 4);
	Pointer p2(2,2);
	Pointer p3 = p1 + p2;
	p3 = p1 - p2;
	cout << p3;
	cout << endl;
	p3 = p1 * p2;
	cout << p3;
	cout << endl;
	p3 = p1 / p2;
	cout << p3;
	cout << endl;
	cin.get();
	return 0;
}

int main2()
{
	Pointer p(4,2);
	Pointer po(2,1);
	Pointer result;
	result = p % po;
	cout << result;
	cout << endl;
	result = p ^ po;
	cout << result;
	cout << endl;
	Pointer* temp=  &po;
	bool buffer = p | po;
	cout << buffer;
	cin.get();
	return 0;
}
int main()
{
	/*Pointer p(3, 1);
	cout << p;
	cout << (2 + Pointer(1, 2));
*/
	Pointer p(1, 2);
	cout << p;
	++p;
	cout << p << endl;
	system("pause");
	return 0;
}