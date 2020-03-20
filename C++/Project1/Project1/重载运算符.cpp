#include <iostream>
#include <string>
#include <fstream>
using namespace std;

class MyComplex
{
public:

	friend ostream & operator << (ostream & out, MyComplex & myc) {
		out << myc.x << "+" << myc.y << "i" << endl;
		return out;
	}

	
	int x;
	int y;
	MyComplex() {
		this->x = 0;
		this->y = 0;
	}
	
	MyComplex(int x, int y) {
		this->x = x;
		this->y = y;
	}
	~MyComplex() {

	}
protected:
private:

};


int main1() {
	MyComplex my(1,2);
	cout << my;
	cin.get();
	return 0;
}
struct temp {
	int a:4;
	string s;
	char* p;
};
enum color{red=0,blue = 127};
int main5()
{
	//color c=color(11);
	//cout << c << endl;
	//int* p;
	//*p = 233333;
//	cout << *p << endl;
	//int* p = NULL;
	//delete(p);
	//cout << (p==NULL) << endl;
	char* p = "hello world";
	cout << p << endl;
	cin.get();
	return 0;
}
int main3()
{
	temp t = {};
	t.a = 11;
	cout <<"t.s"<< t.a << endl;
	cin.get();
	return 0;
}
int main4()
{
	/*int a = 30;
	cout << hex;
	cout << a << endl;*/
	//cout << "hello world" "world" << endl;
	string s = "hello ";
	//char *p = "hello";
	//char p[20] = "hello";
	//char s[10] = "world";
	//strcat_s(p,20,s);
	//cout << p << endl;
	/*for (int i = 0; i < s.length(); i++)
	{
		cout << s[i];

	}
	cout << endl;*/

	ofstream out;
	out.open("D:/test.txt");
	//out.precision(2);
	//out.setf(ios_base::showpoint);
	out << "hellojjjj" ;
	out.close();
	cin.get();
	return 0;
}
void static_func() {
	static int a = 30;
	cout << a++ << endl;
}
int main__()
{

	/*static_func();
	static_func();
	static_func();
	static_func();
*/
	double a = 3;
	cout << a << endl;
	cin.get();
	return 0;
}


