#include <iostream>
#include <array>
int main() {
	std::array<int, 5> a = { 1,2,3,4,5 };
	std::array<int, 5> b;
	b = a;
	int a_old[5] = { 1,2,3,4,5 };
	int b_old[5];
//	b_old = a_old;
	std::cin.get();
	return 0;
}