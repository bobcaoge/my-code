#include <iostream>
using std::cout;
using std::cin;
using std::endl;
class Base
{
private:
	int data;
public:
	Base(int d = 0);
	void p_data();
};
Base::Base(int d) {
	data = d;
}
void Base::p_data()
{
	cout << data << endl;;
}

class SubBase :public Base
{
private:
	int subdata;
public:
	SubBase(int sd=0, int d=0);
	SubBase(int sd, const Base& b);
	void p_info();
};
SubBase::SubBase(int sd = 0, int d = 0):Base(d), subdata(sd)
{
}
SubBase::SubBase(int sd, const Base& b):Base(b), subdata(sd)
{
}
void SubBase::p_info()
{
	p_data();
	cout << subdata << endl;
}
int main()
{
	cin.get();
	return 0;
}