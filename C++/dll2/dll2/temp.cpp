#include <iostream>

using namespace std;
class __declspec(dllexport) Test
{
public:
	int add(int a, int b)
	{
		return a + b;
	}
	int subtract(int a, int b)
	{
		return a - b;
	}
};
