# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return -1

        nums = [_ for _ in str(n)][-1::-1]
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                self.manage(nums, i)
                # get head nums
                nums_1 = "".join(nums[i:][-1::-1])
                # get tail nums
                nums_2 = "".join(sorted(nums[:i]))
                # print(nums_1, nums_2)
                result = int(nums_1+nums_2)
                return -1 if result > 2**31-1 else result

        return -1

    def manage(self, nums, i):
        old = nums[i]
        nums[i], nums[i-1] = nums[i-1], nums[i]
        for index in range(i-2, -1, -1):
            if old < nums[index] < nums[i]:
                nums[index], nums[i] = nums[i], nums[index]



def main():
    s = Solution()
    # print(s.nextGreaterElement(12))
    print(s.nextGreaterElement(1212124211))
    print(s.nextGreaterElement(12443322))
    print(s.nextGreaterElement(123456))
    print(s.nextGreaterElement(1999999999))


if __name__ == "__main__":
    main()
