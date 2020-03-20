#include<math.h>
#include<algorithm>
class Solution {
public:
	bool divisorGame(int N) {
		bool Alice[1001] = { false };
		Alice[1] = false;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j < i; j++) {
				if (Alice[j] == false && i % (i - j) == 0) {
					Alice[i] = true;
					break;
				}
			}

		}
		return Alice[N];


	}
	/*
	O(n*sqrt(n))
	*/
	bool divisorGame_2(int N) {
		bool Alice[1001] = { false };
		Alice[0] = true;
		Alice[1] = false;
		for (int i = 2; i <= N; i++) {
			for (int j = 1; j <= int(sqrt(i)); j++) {
				if (i % j == 0 && (Alice[i - j] == false || Alice[i - i / j] == false)) {
					Alice[i] = true;
					break;
				}
			}

		}
		return Alice[N];
	}
};