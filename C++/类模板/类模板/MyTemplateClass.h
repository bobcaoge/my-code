#pragma once
template<typename T>
class MyTemplateClass
{
public:
	MyTemplateClass();
	~MyTemplateClass();
	void run(T t);
	T get();
private:
	T t;
};

