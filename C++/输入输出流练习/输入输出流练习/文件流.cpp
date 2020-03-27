#include <iostream>
#include <fstream>
using namespace std;
struct temp
{
	char *p = "";
	int a = 10;
	double b = 1.1111111111111111111111;
	char h = 'c';
};
int main()
{
	/*
	ofstream out;
	out.open("temp.txt");
	out << "hello" << endl;
	out << "second line" << endl;
	out << "third line" << endl;
	out.close();

	ifstream in;
	in.open("temp.txt");
	//char* ss = new char[20];
	char* ss[10];
	char s[20];
	cout << sizeof(s) <<":"<< sizeof(ss) << endl;
	in.getline(s, 20);
	cout << s << endl;
	cout << "===========" << endl;
	cout << sizeof(temp) << endl;
	double a = 10;
	cout << sizeof(a) << endl;
*/
	/*temp t;
	t.p = "aaaaaaaaaaaaaaaa";
	char *p = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb";
	cout << sizeof(temp) << endl;
	ofstream out("a.bin", ios::binary);
	out.write((char*)(&t), sizeof(temp));
	//out.write(p, sizeof(p));
	out.close();
*/
	ifstream in("a.bin", ios::binary);
	temp tt;
	char *pp = "";
	in.read((char*)(&tt), sizeof(temp));
	//in.read(pp, sizeof(pp));
	in.close();
	cout << tt.a << endl;

	cin.get();
	return 0;
}













