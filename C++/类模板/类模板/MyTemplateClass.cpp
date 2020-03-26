#include "MyTemplateClass.h"

template<typename T>
MyTemplateClass<T>::MyTemplateClass()
{
}

template<typename T>
MyTemplateClass<T>::~MyTemplateClass()
{
}
template<typename T>
void MyTemplateClass<T>::run(T t){
	std::cout << "run" << std::endl;
}
template<typename T>
T MyTemplateClass<T>::get(){
	std::cout << "get" << std::endl;
	return T();
}
