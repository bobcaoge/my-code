# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        m = {}
        def dfs(i):
            if m.get(i, 0) == 0:
                ret = 1
                for j in range(i-1, max(0, i-d)-1, -1):
                    if arr[j] < arr[i]:
                        ret = max(ret, dfs(j)+1)
                    else:
                        break
                for j in range(i+1, min(i+d+1, len(arr))):
                    if arr[j] < arr[i]:
                        ret = max(ret, dfs(j)+1)
                    else:
                        break
                m[i] = ret
            return m[i]
        res = 0
        for i in range(len(arr)):
            res = max(res,dfs(i))
        return res


def main():
    s = Solution()
    print(s.maxJumps([6,4,14,6,8,13,9,7,10,6,12], d = 2))


if __name__ == "__main__":
    main()
