#include <iostream>
#include <sstream>
#include <string>
using namespace std;
struct student
{
	string name;
	int age;
	string addr;
};
int mainstring()
{
	string s = "hello C++";
	string stu_s = "black 12 Beijing";
	istringstream input(stu_s);
	student stu;
	input>> stu.name >> stu.age >> stu.addr;
	cout << stu.name << " " << stu.age << " " << stu.addr << endl;
	ostringstream output;
	output << "abc" << 124959 << "hello" << endl;
	string dest;
	dest = output.str();
	//cout << output.str() << endl;
	cout << dest;
	cin.get();
	return 0;
}