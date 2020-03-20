#include <iostream>
#include <set>
#include <vector>
#include <string>
using namespace std;

class Person {
friend bool operator<(const Person& p1, const Person & p2);
private:
	int age;
	string name;
public:
	int getAge() {
		return this->age;
	}
	string getName() {
		return this->name;
	}
	Person(int age, string name) {
		this->age = age;
		this->name = name;
	}
	
};
bool operator<(const Person& p1, const Person& p2) {
	if (p1.age <= p2.age) {
		return true;
	}
	return false;
}
/*
void operator=(Person another) {
		this->age = another.getAge();
		this->name = another.getName();
	}
*/
void print_set(set<int> s) {
	for (set<int>::iterator it = s.begin(); it != s.end(); it++) {
		cout << *it << " ";
	}
	cout << endl;
	cout << endl;
}
int main2() {
	set<int> s;
	set<int>::iterator it;
	pair<set<int>::iterator, bool> ret;
	s.insert(3);
	// insert �����ֲ��뷽ʽ  ����set������ģ������ڲ����Զ������ʱ��Ҫ����<
	// 1�����뵥������
	s.insert(2);
	print_set(s);
	// 2������λ�ò��룬���������һ�������ڸ�λ�ú��棨��Ϊset������ģ�ÿ�β���󶼻���������
	it = s.insert(2).first;
	s.insert(it, 20);
	print_set(s);
	// 2���������ʼ��ַ��������ַ֮���ֵ������ұ�
	int arr[] = { 1,2,30 };
	s.insert(arr, arr + 3);
	print_set(s);
	ret = s.insert(3);
	cout << ret.second << endl;
	ret = s.insert(3000);
	cout << ret.second << endl;


	//���� ����һ�������� ����ҵ������ظ�Ԫ�صĵ����������򷵻�set.end();
	cout << "find" << endl;
	it = s.find(9);
	cout << (it == s.end()) << endl;

	// ɾ�� �Ȳ�������ҵ���ɾ�������û�ҵ����Ͳ�Ҫִ��ɾ�� ��ɾ��������erase��iterator��
	cout << "delete" << endl;
	it = s.find(3);
	if (it != s.end()) {
		s.erase(it);
	}
	print_set(s);
	set<Person> persons;
	//persons.emplace(Person(11, "white"));
	//cout << (p < Person(12, "a")) << endl;
	persons.insert(Person(11, "a"));
	persons.insert(Person(12, "b"));
	persons.insert(Person(13, "c"));
	persons.emplace(14, "d");
	persons.emplace_hint(persons.begin(), 15, "d");
	cout << persons.size() << endl;
	for (auto it : persons) {
		cout << it.getAge() << " " << it.getName() << endl;;
	}
	








	cin.get();
	return 0;
}
