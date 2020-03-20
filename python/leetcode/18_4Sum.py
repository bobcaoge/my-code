# /usr/bin/python3.6
# -*- coding:utf-8 -*-



class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = {}
        # keys = set()
        for num in nums:
            m[num] = m.get(num, 0) + 1
            # keys.add(num)
        keys = list(m.keys())

        ret = set()
        # keys = list(keys)
        length = len(keys)
        for i in range(length):
            m[keys[i]] -= 1
            for j in range(length):
                if m[keys[j]] == 0:
                    continue
                m[keys[j]] -= 1
                buff1 = keys[i]+keys[j]
                for k in range(length):
                    if m[keys[k]] == 0:
                        continue
                    cur = buff1 + keys[k]
                    m[keys[k]] -= 1
                    another = target - cur
                    if m.get(another, 0) != 0:
                        ret.add(tuple(sorted((keys[i], keys[j], keys[k], another))))
                    m[keys[k]] += 1
                m[keys[j]] += 1
            m[keys[i]] += 1
        return [list(x) for x in ret]





def main():
    s = Solution()


if __name__ == "__main__":
    main()
