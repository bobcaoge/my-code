#include <iostream>
#include<map>
#include<vector>
#include <string>
using namespace std;
void print_vector(vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;

}
int main1() {
	/*
	map<int, int> m;
	int arr[] = { 1,2,3,4,6,7,9,5,3,5,7 };
	m[1] = 3;
	cout << m[1] << endl;
	cout << m[2] << endl;
	map<string, string> m;
	m["a"] = "abc";
	cout << m["a"] <<  endl;
*/
/*
	map<int, char> m;
	m[1] = 'c';
	cout << m[1] << endl;
	cout << m[3] << endl;
*/
	/*
	map<int, int> m;
	vector<int> arr = { 1,2,3,4,6,7,9,5,3,5,7 };
	for (int i = 0; i < arr.size(); i++) {
		m[arr[i]] = m[arr[i]] + 1;
	}
	for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
		cout << it->first << " : " << it->second << endl;

	}
	cout << endl;
	map<int, int>::iterator it;
	it = m.find(100);
	cout << (it == m.end()) << endl;
	//m.erase(it);
	for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
		cout << it->first << " : " << it->second << endl;
	}
*/
	vector<int> arr = { 1,2,3,4,6,7,9,5,3,5,7 };
	map<int, vector<int>> m;

	for (int i = 0; i < arr.size(); i++) {
			m[arr[i]].push_back(arr[i]);
	}
	for (map<int, vector<int>>::iterator it = m.begin(); it != m.end(); it++) {
		cout << it->first << " : ";
		print_vector(it->second);
	}
	cin.get();
	return 0;
}