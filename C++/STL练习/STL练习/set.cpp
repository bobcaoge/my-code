#include <iostream>
#include <set>
#include <string>
#include "Student.h"
using namespace std;
class Compare{
public:
	bool operator()(Student s1, Student s2){
		return s1.age < s2.age;
	}
};
int mainset(){
	Student stu(3, "bob");
	set<Student, Compare> s;
	for (int i = 0; i < 10; i++){
		s.insert(Student(i, "bob" + string(1, i+97)));
	}
	for (auto buff : s){
		cout << buff.name << " " << buff.age << endl;
	}
	cin.get();
	return 0;
}