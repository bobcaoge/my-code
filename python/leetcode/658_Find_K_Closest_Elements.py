# /usr/bin/python3.6
# -*- coding:utf-8 -*-



class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k <= 0:
            return []
        index_of_x = 0
        for i, num in enumerate(arr):
            if num <= x:
                index_of_x = i
            else:
                if num - x < x - arr[index_of_x]:
                    index_of_x = i
                break

        index_of_left = index_of_x - 1
        index_of_right = index_of_x + 1
        ret = [arr[index_of_x]]
        k -= 1
        while index_of_left >= 0 and index_of_right < len(arr) and k > 0:
            if abs(arr[index_of_left] - x) <= abs(arr[index_of_right] - x):
                # ret.append(arr[index_of_left])
                ret.insert(0, arr[index_of_left])
                index_of_left -= 1
            else:
                ret.append(arr[index_of_right])
                index_of_right += 1
            k -= 1
        if k > 0 and index_of_left >= 0:
            ret = arr[index_of_left-k+1:index_of_left+1] + ret
        if k > 0 and index_of_right < len(arr):
            ret += arr[index_of_right:index_of_right+k]
        # return sorted(ret)
        return ret


def main():
    s = Solution()
    # print(s.findClosestElements([1,2,3,4,5], 4, 3))
    # print(s.findClosestElements([1,2,3,4,5,7,8,9,10], 4, 6))
    # print(s.findClosestElements([1], 1, 1))
    print(s.findClosestElements([1,2,3,4,5], 4, 11))


if __name__ == "__main__":
    main()
