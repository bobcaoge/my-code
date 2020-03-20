#include <math.h>
using namespace std;
class Solution {
public:
	bool judge(int num) {
		if (num == 1) {
			return false;
		}
		for (int i = 2; i <= sqrt(num); i++) {
			if (num % i == 0) {
				return false;
			}

		}
		return true;
	}
	int to_mod = 1000000007;
	int numPrimeArrangements(int n) {
		int num_of_primes = 0;
		for (int i = 1; i <= n; i++) {
			if (judge(i)) {
				num_of_primes++;
			}
		}
		long ret = 1;
		for (int i = 2; i <= num_of_primes; i++) {
			ret = (ret % to_mod)*(i%to_mod) % to_mod;
		}
		for (int i = 2; i <= (n - num_of_primes); i++) {
			ret = (ret % to_mod)*(i%to_mod) % to_mod;
		}
		return ret;

	}
};