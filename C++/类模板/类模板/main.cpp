#include <iostream>
#include "MyTemplateClass.h"
#include "MyTemplateClass.cpp"
using namespace std;

int main(){
	MyTemplateClass<int> mtc;
	mtc.run(2);
	mtc.get();

	cin.get();
	return 0;
}