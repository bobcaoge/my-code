#include <iostream>
#include <hash_set>
#include <hash_map>
using namespace std;
int mainmain(){
	/*
	char *p[] = { "abcd", "cde", "cde", "cde", "cde", "cde" };
	cout << sizeof(p) << endl;
	char* pp = "abacd";
	cout << sizeof(pp) << endl;
	cout << typeid(p).name() << endl;
	cout << pp << " : " << *pp << endl;
	*/
	hash_set<int> a;
	hash_map<int, int> b;
	a.insert(2);
	a.insert(4);
	a.insert(3);
	a.insert(5);
	a.insert(9);
	for (auto data : a){
		cout << data<< endl;
	}
	cin.get();
	return 0;
}