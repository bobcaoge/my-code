#include<random>
using namespace std;
int rand7() {
	return rand() % 7 + 1;
}
class Solution {
public:
	int rand6() {
		return rand7() - 1;
	}
	int rand10() {
		int a = rand6();
		int b = rand6();
		while (a * 7 + b > 39) {
			a = rand6();
			b = rand6();
		}
		return (a * 7 + b) % 10 + 1;
	}
};