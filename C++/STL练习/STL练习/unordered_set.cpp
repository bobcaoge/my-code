#include <iostream>
#include <unordered_set>
#include <string>
#include <functional>
#include "Student.h"
using namespace std;
class Compare{
public:
	bool operator()(Student s1, Student s2){
		return s1.age < s2.age;
	}
};
class Hash{
public:
	size_t operator()(Student s){
		return hash<string>()(s.name + to_string(s.age));
	}
};
int main(){
	Student stu(3, "bob");
	unordered_set<Student, Hash> s;

	for (int i = 0; i < 10; i++){
	s.insert(Student(i, "bob" + string(1, i+97)));
	}
	for (auto buff : s){
		cout << buff.name << " " << buff.age << endl;
	}
	cin.get();
	return 0;
}