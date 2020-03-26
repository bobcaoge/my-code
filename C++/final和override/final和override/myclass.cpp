#include <iostream>
using namespace std;
class Base
{
public:
	virtual void run(int a){
		cout << a << endl;
	}
	virtual void last(int a) final{
		cout << "last" << a << endl;
	}
};

class SubBase : public Base
{
public:
	void run(int a) override{
		cout << "subBase" << endl;
	}
};
int main(){
	Base* b = new SubBase();
	b->run(2);
	b->last(3);
	cin.get();
	return 0;
}










