#include <iostream>
#include <cstring>
#include "StringBad.h"

using std::cout;
using std::cin;
using std::endl;

void callme1(StringBad& s)
{
	cout <<"call "<< s<< endl;
}
void callme2(StringBad s)
{
	cout <<"call "<< s<< endl;
}
int main()
{
	{
	//StringBad test("hello word");
	/*callme1(test);
	callme2(test);
	StringBad ano = test;
	StringBad anoo = test;
*/
	char a[20] = "hello world";
	cout << a << endl;

	}

	cin.get();
	return 0;
}
