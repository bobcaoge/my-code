#include <string>
#include <iostream>
using std::cout;
using std::cin;
using std::endl;
void run() {}

template<typename T, typename...Args>
void run(T value, Args...args) {
	cout << value << endl;
	run(args...);
}
void main() {
	int a = 1;
	int b = 2;
	int c = 3;
	char d = 'd';
	std::string s = "hello";
	run(a, b, c, d, s);
	cin.get();
	
}