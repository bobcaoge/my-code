#include <iostream>
#include <iomanip>
#include <string> 
using namespace std;
int mainaadfdsfa()
{
	//1����
	//1.1�� ����
	cout << hex;
	cout << 15 << endl;
	cout << oct;
	cout << 101 << endl;
	cout << dec;
	cout << 010 << endl;
	//1.2�� ��Ч����
	cout.precision(4);
	cout << 1.1234456789 << endl;
	//�ַ���
	//�ַ������
	string s = "hello";
	cout.setf(ios::left);
	cout.fill('*');
	cout.width(10);
	cout << s << endl;
	


	cin.get();
	return 0;
}