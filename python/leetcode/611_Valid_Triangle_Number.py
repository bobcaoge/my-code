# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type m: List[int]
        :rtype: int
        """
        record = [0]*2000
        for num in nums:
            record[num] += 1
        record[0] = 0
        m = record.copy()
        for i in range(1, 1000):
            record[i] += record[i-1]
        # 不等边，不等腰
        ret = 0
        traverse = sorted(list(set(nums)))

        for index, i in enumerate(traverse):
            for j in traverse[index+1:]:
                ret += (record[i+j-1]-record[j])*m[i]*m[j]

        print(ret)
        # 等腰
        for i in traverse:
            ret += (record[2*i-1] - m[i])*(m[i]-1)*m[i]/2
        print(ret)
        # 等边
        for i in traverse:
            ret += m[i]*(m[i]-1)*(m[i]-2)/6
        return ret


def main():
    s = Solution()
    # print(s.triangleNumber([2,3,4,4,5,6,7,8,9]))
    # print(s.triangleNumber([2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,5,6,7,7,7,7,7,7,8,9]))
    # print(s.triangleNumber([0,0,0,0]))
    print(s.triangleNumber([0,1,1]))


if __name__ == "__main__":
    main()
