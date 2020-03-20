#pragma once
#include <iostream>
using std::ostream;
class Pointer
{
private:
	double x;
	double y;
public:
	Pointer(double x=0, double y=0);
	~Pointer();
	Pointer operator +(const Pointer & pointer) const;
	Pointer operator -(const Pointer & pointer) const;
	Pointer operator *(const Pointer & pointer) const;
	Pointer operator /(const Pointer & pointer) const;

	Pointer operator %(const Pointer & pointer) const;
	Pointer operator ^(const Pointer & pointer) const;
	Pointer* operator &(Pointer & Pointer) const;
	bool operator |(const Pointer & pointer) const;
	//后缀++
	Pointer operator ++(int);
	//前缀++
	Pointer operator ++();
	//后缀--
	Pointer operator --(int);
	//前缀--
	Pointer operator --();
	friend Pointer operator+(double x, Pointer & p);
	friend ostream& operator<<(ostream & os, const Pointer & pointer);
	//void operator<<(Pointer & p);

};
