class Solution {
public:
	int tribonacci(int n) {
		int nums[3] = { 0 , 1, 1 };
		if (n < 3) {
			return nums[n];
		}
		n -= 2;
		int buff = 0;
		while (n != 0) {
			buff = nums[0] + nums[1] + nums[2];
			nums[0] = nums[1];
			nums[1] = nums[2];
			nums[2] = buff;
			n -= 1;
		}
		return nums[2];

	}
};