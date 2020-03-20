#include <iostream>
#include <string.h>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
class MyString{
	private:
		char *s;
	
	public:
		MyString(){
			s = new char[1024];
//			cout<<"common MyString()"<<endl; 
		}
		MyString(const MyString &it){
//			cout<<"copy MyString"<<endl;
			s = new char[1024];
			memset(s, 0, 1024);
			strcpy(this->s, it.s);
		}
		MyString(char *s){
//			cout<<"MyString with canshu"<<endl;
			this->s = new char[1024];
			memset(this->s, 0, 1024);
			strcpy(this->s, s);
		}
		~MyString(){
//			cout<<"~MyString"<<endl;
		}
		char *get_s(){
			return this->s;
		}
		const void set_s(char *s) const{
			strcpy(this->s, s);
		} 
		
		MyString operator +(const MyString &it){
			strcat(this->s,it.s);
			return *this;
		} 
		MyString operator +(const char *c){
			strcat(this->s, c);
			return *this;
		}
		friend MyString operator +(const char* c, const MyString &it);
		friend bool operator ==(const char*c, const MyString &it);
};

MyString operator +(const char* c, const MyString &it){
	MyString s("");
	strcat(s.s, c);
	strcat(s.s, it.s);
	return s;
	
}
bool operator ==(const char*c, const MyString &it){
	if (strcmp(c, it.s)==0)
		return true;
	return false;
		
}

int main(int argc, char** argv) {
	MyString s;
	s.set_s("hello ");
	MyString ss(s);
	ss.set_s(" world!");
//	MyString sss("hello world");// = new MyString("hello world");
//	cout<<s.get_s()<<endl;
//	cout<<ss.get_s()<<endl;
//	cout<<sss.get_s()<<endl;
//	s = s + ss;
//	s = s + " world!!!";
//	s = "hello " + s;
	cout<<s.get_s()<<endl;
	cout<<("hello " == s)<<endl;
	cout<<("hello"== s)<<endl;
	return 0;
}
