#pragma once
#include<string>
#include <functional>
class Student
{
public:
	Student();
	Student(int age_, std::string name_) :age(age_), name(name_){};
	~Student();
	bool operator<(Student s){
		return this->age < s.age;
	}
	bool operator==(const Student& s)const{
		return this->age == s.age && this->name == s.name;
	}

	int age;
	std::string name;
};

