#pragma once
#include <iostream>
using std::ostream;
using std::cout;
using std::endl;
class StringBad
{
private:
	char* str;
	int len;
	static int num_of_str;
public:
	friend ostream& operator<<(ostream& os, StringBad & s);
	StringBad(const char* s);
	~StringBad();

};

