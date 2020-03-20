#include "Pointer.h"
#include <iostream>
#include <cmath>
using std::ostream;
Pointer::Pointer(double x, double y)
{
	this->x = x;
	this->y = y;
}




Pointer Pointer::operator +(const Pointer & pointer) const
{
	Pointer temp;
	temp.x = x + pointer.x;
	temp.y = y + pointer.y;
	return temp;
}
Pointer Pointer::operator -(const Pointer & pointer) const
{
	Pointer temp;
	temp.x = this->x - pointer.x;
	temp.y = this->y - pointer.y;
	return temp;
}
Pointer Pointer::operator *(const Pointer & pointer) const
{
	Pointer temp;
	temp.x = this->x*pointer.x;
	temp.y = this->y*pointer.y;
	return temp;

}
Pointer Pointer::operator /(const Pointer & pointer) const
{
	Pointer temp;
	temp.x = this->x/pointer.x;
	temp.y = this->y/pointer.y;
	return temp;
}
Pointer::~Pointer()
{
}

Pointer Pointer::operator %(const Pointer & pointer) const
{
	Pointer ret;
	ret.x = static_cast<int>(this->x)%static_cast<int>(pointer.x);
	ret.y = static_cast<int>(this->y)%static_cast<int>(pointer.y);
	return ret;
}
Pointer Pointer::operator ^(const Pointer & pointer) const
{
	Pointer ret;
	ret.x = pow(this->x, pointer.x);
	ret.y = pow(this->y, pointer.y);
	return ret;
}
Pointer* Pointer::operator &(Pointer & pointer) const
{
	Pointer* ret;
	ret = &pointer;
	return ret;

}
bool Pointer::operator |(const Pointer & pointer) const
{
	if (this->x < 0 || pointer.x < 0 || this->y < 0 || pointer.y < 0) {
		return false;
	}
	return true;
}

Pointer operator+(double x, Pointer & p) {

	Pointer ret;
	ret.x = x + p.x;
	ret.y = x + p.y;
	return ret;
}
ostream& operator<<(ostream & os, const Pointer & pointer)
{
	os<< pointer.x << " " << pointer.y;
	return os;
}
Pointer Pointer::operator ++(int)
{
	Pointer temp;
	temp.x = this->x++;
	temp.y = this->y++;
	return temp;
}
Pointer Pointer::operator ++()
{
	this->x++;
	this->y++;
	return *this;
}
//ºó×º--
Pointer Pointer::operator --(int)
{
	this->x--;
	this->y--;
	return *this;
}
//Ç°×º--
Pointer Pointer::operator --()
{
	this->x--;
	this->y--;
	return *this;
}