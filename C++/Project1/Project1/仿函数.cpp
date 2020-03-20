#include <iostream>
#include <functional>
#include <stdlib.h>
#include <memory>
using namespace std;
using namespace std::placeholders;
struct Mystruct
{
	void add1(int a, int b)
	{
		cout << a + b << endl;
	}
};
int main() {
	/*Mystruct ms;
	auto fun = bind(&Mystruct::add1, &ms, _1, _2);
	fun(2, 4);
*/		double *p = new double;//为指针分配内存

	double* p = new double();
	auto_ptr<double> autop(p);
	unique_ptr<double> up(new double);
	
	system("pause");
	return 0;
}