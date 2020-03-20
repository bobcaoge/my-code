#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;
class Data {
public:
	int num;
	Data(int num=0) {
		this->num = num;
	}
};
int main5() {
	//unordered_set<Data> data;
	unordered_set<int> data, data_bak;
	for (int i = 0; i < 9; i++) {
		//data.insert(Data(i));
		data.insert(i);
	}
	/*
	for (Data d : data) {
		cout << d.num << " ";
	}*/
	for (auto d : data) {
		cout << d<< " ";
	}
	cout << endl;
	data_bak = data;
	cout << &data << ": " << &data_bak << endl;
	cin.get();
	return 0;
}