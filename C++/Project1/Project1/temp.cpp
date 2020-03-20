// ConsoleApplication1.cpp : 定义控制台应用程序的入口点。
//


#include <iostream>
#include < stdlib.h>
#include <string>
#include <locale>
#include <functional>
#include <array>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
struct Bigdatacalc {
private:
	char* data1;
	char* data2;
public:
	void init(char* data1, char* data2) {
		this->data1 = data1;
		this->data2 = data2;
	}
	char* getplusResult() {
		int length1 = strlen(data1);
		int length2 = strlen(data2);
		//cout<< "length1: "  << length1<< "lenght2:"  << length2 << endl;
		int* buffer = (int*)malloc(sizeof(int)*(length1 + length2));
		memset(buffer, 0,sizeof(int)*(length1 + length2));
		//cout << *buffer << endl;
		//累加
		for (int i = 0; i < length1; i++) {
			for (int j = 0; j < length2; j++) {
				buffer[i + j + 1] += (data1[i] - '0')*(data2[j] - '0');
			}
		}
		
		
		//进位
		
		for (int j = length1+length2 - 1; j > -1; j--) {
			buffer[j - 1] += buffer[j] / 10;
			buffer[j] %= 10;
		}

		int i = 0;
		while (buffer[i] == 0) {
			i++;
		}
		char* ret = (char*)malloc(sizeof(char*)*(length1 + length2 - i+1));
		int j;
		int length = length1 + length2 - i + 1;
		for (j = 0; j < length-1; j++, i++) {
			ret[j] = buffer[i]+'0';

		}
		ret[j] = '\0';
		
		return ret;
	}

};
template <typename T> T add(T a, T b) {
	return a + b;
}
/*void operator delete(void* p)
{
	cout << "全局被调用 内存被回收" << endl;
	free(p);
}
*/

/*void *operator new(size_t size) {
	cout << "全局被调用 内存被分配" << endl;
	if (size == 0)
	{
		return 0;
	}
	void *p = malloc(size);
	return p;
}
*/
class Hello
{
public:
	Hello()
	{
		cout << "hello 被创建" << endl;
	}
	~Hello()
	{
		cout << "hello 被销毁" << endl;
	}
	static void * operator new(size_t size) {
		cout << "局部被调用 内存被分配" << endl;
		
		Hello* h = ::new Hello;
		return h;
	}
	static void operator delete(void* p)
	{
		cout << "局部被调用， 内存被回收" << endl;
		 ::delete(p);
	}
};

int main1() {
	//int* p = new int;
	//delete(p);
	Hello* h = new Hello;
	delete(h);
	//cout << "hello world" << endl;
	system("pause");
	return 0;
}
int main2() {
	char* data1 = new char[100];
	char* data2= new char[100];
	cin >> data1;
	cin >> data2;
	Bigdatacalc bd;
	bd.init(data1, data2);
	cout << bd.getplusResult() << endl;;
	system("pause");
	return 0;
}

class Myclass {
public:
	int a;
	double c;
	int b;
};
template<class T>
void com(T arg)
{
	arg++;
}
int main() {
	//cout << add<int>(1, 2) << endl;
	//cout << add<double>(1, 2.0) << endl;
	//cout << add<float>(1, 2.0) << endl;
//	setlocale(LC_ALL, "chs");
//	wchar_t *p = L"hello world";
//	wchar_t *d = L"北京hello world";
//	wcout << p << endl;
//	wcout << d << endl;
	//setlocale(LC_ALL, "chs");//设置本地化
	//wchar_t *p1 = L"123456123123qweqeqe";
	//std::wcout << p1 << std::endl;
	//wchar_t *p2 = L"北京123456";
	//std::wcout << p2 << std::endl;
//`	function <double(double)> fun = [](double a) {return a*a; };
//	cout << fun(23) << endl;
	//cout << sizeof(Myclass) << endl;
	/*array<string, 4> arr = { "calc", "notepad", "tasklist","mspaint" };
	for (int i = 0; i < 4; i++) {
		cout << arr[i] << endl;
	}*/
	/*array<string, 4> arr = { "calc", "notepad", "tasklist","mspaint" };
	array<string, 4>::iterator arrbegin, arrend;

	arrbegin = arr.begin();
	arrend = arr.end();
	while (arrbegin != arrend) {
		cout << *arrbegin << " ";
		arrbegin++;
	}
	cout << endl;
	array<string, 4>::reverse_iterator rarrbegin, rarrend;

	rarrbegin = arr.rbegin();
	rarrend = arr.rend();
	while (rarrbegin != rarrend) {
		cout << *rarrbegin << " ";
		rarrbegin++;
	}
	cout << endl;
	vector<string> a;
	a.push_back("calc");
	a.push_back("notepad");
	a.push_back("tasklist");
	a.push_back("mspaint");
	vector<string>::iterator begin = a.begin(); 
	vector<string>::iterator end = a.end(); 
	while(begin != end) {
		cout << *begin << " ";
		begin++;
	}
	cout << endl;
	vector<string>::reverse_iterator rbegin, rend;
	rbegin = a.rbegin();
	rend = a.rend();
	while (rbegin != rend) {
		cout << *rbegin << " ";
		rbegin++;
	}
	cout << endl;
	
	
	tuple<int, double, char*> tup = { 1, 1.1, "helllo" };
	cout << get<0>(tup) << endl;

	vector<int> vec(4);
	for (int i = 0; i < vec.size(); i++) {
		cout << vec.at(i) << endl;
	}
	vec.push_back(3);
	vec.push_back(4);
	vec.push_back(5);
	vec.push_back(6);
	vec.push_back(7);
	/*vec.erase(vec.begin() + 4);
	cout << "*******************" << endl;
	for (int i = 0; i < vec.size(); i++) {
		cout << vec.at(i) << endl;
	}

	int ret = 0;
	for_each(vec.begin(), vec.end(), [&ret](int x) {ret += x; });
	//cout << ret << endl;
*/
	int count = 1;
	int & rcount = count;
	com(ref(count));
	cout << count << endl;
	system("pause");
	return 0;
};
