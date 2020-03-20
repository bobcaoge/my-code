#include "StringBad.h"
int StringBad::num_of_str = 0;
StringBad::StringBad(const char * s)
{
		len = strlen(s);
		str = new char[len + 1];
		strcpy_s(str, len+1, s);
		cout << "create: " <<num_of_str<< str << endl;
		cout << endl;
		num_of_str++;
	}

StringBad::~StringBad()
{
	cout << "=============" << endl;
	cout << "delete " << str << endl;
	delete[] str;
	num_of_str--;
	cout << num_of_str << " object is left" << endl;
	cout << "=============" << endl;
}


ostream& operator<<(ostream& os, StringBad & s)
{
	os << s.str << endl;
	return os;
}