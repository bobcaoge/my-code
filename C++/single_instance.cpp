#include <iostream>
#include <string.h>
using namespace std;
class Single
{
	private:
		int age;
		char *name;
		static Single *self;
		Single();
		Single(const int age, const char* name);
		Single(const Single &it);
	public:
		static Single *get_intance(const int age, const char* name);
		static Single *delete_intance();
		const int get_age() const;
		const char* get_name() const;
		void set_age(int age);
		void set_name(char *name);
};
Single *Single::self = NULL;
 Single *Single::delete_intance(){
	if (self != NULL){
		delete(self);
		self = NULL;
	}
}
Single *Single::get_intance(const int age, const char* name)
{
	if (self == NULL){
		self = new Single(age, name);
	}
	
	return self;
	
}
Single::Single(){
	
}
Single::Single(const int age, const char* name){
	this->age = age;
	int len = strlen(name);
	this->name = new char[len + 1];
	strcpy(this->name, name);
	this->name[len + 1] = '\0';
}
Single::Single(const Single &it){
	this->age = it.get_age();
	int len = strlen(it.get_name());
	this->name = new char[len + 1];
	strcpy(this->name, it.get_name());
	this->name[len + 1] = '\0';
}
const int Single::get_age() const{
	return this->age;
}

const char *Single::get_name() const{
	return name;
}
void Single::set_age(int age){
	this->age = age;
}
void Single::set_name(char *name){
	int len = strlen(name);
	this->name = new char[len + 1];
	strcpy(this->name, name);
	this->name[len+1] = 0;
}
int main()
{
	Single *s = Single::get_intance(13, "Black");
	cout<<s->get_age()<<" "<<s->get_name()<<endl;
	s = Single::get_intance(14, "White");
    cout<<s->get_age()<<" "<<s->get_name()<<endl;
    
    Single::delete_intance();
    s = Single::get_intance(14, "Alice");
    cout<<s->get_age()<<" "<<s->get_name()<<endl;
    
	return 0;
} 
