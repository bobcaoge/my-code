# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def sum_of_division(divisor):
            ret = 0
            for num in nums:
                a, b = divmod(num, divisor)
                ret += a + (1 if b > 0 else 0)
            return ret

        start = 1
        end = 2**31
        mid = (start + end) // 2
        ret = end
        while start <= end:
            # 如果结果大于门限值，说明除数过小，需要增大
            if sum_of_division(mid) > threshold:
                start = mid + 1
            # 如果结果小于等于门限值，说明此时[mid，end]里面的所有值均符合，但是[start， mid]中还可能存在更小的
            else:
                ret = min(ret, mid)
                end = mid - 1
            mid = (start + end) // 2

        return ret


def main():
    s = Solution()
    print(s.smallestDivisor(nums = [1,2,5,9], threshold = 6))
    print(s.smallestDivisor([2,3,5,7,11], threshold = 11))
    print(s.smallestDivisor(nums = [19], threshold = 5))
    print(s.smallestDivisor([962551,933661,905225,923035,990560],10))


if __name__ == "__main__":
    main()
