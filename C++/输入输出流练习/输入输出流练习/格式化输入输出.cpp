#include <iostream>
#include <iomanip>
#include <string> 
using namespace std;
int mainaadfdsfa()
{
	//1数字
	//1.1、 进制
	cout << hex;
	cout << 15 << endl;
	cout << oct;
	cout << 101 << endl;
	cout << dec;
	cout << 010 << endl;
	//1.2、 有效数字
	cout.precision(4);
	cout << 1.1234456789 << endl;
	//字符串
	//字符串填充
	string s = "hello";
	cout.setf(ios::left);
	cout.fill('*');
	cout.width(10);
	cout << s << endl;
	


	cin.get();
	return 0;
}