# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import time


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []
        def dfs(exp, res_of_exp, right, last):
            if not right:
                if res_of_exp == target:
                    ret.append(exp)
                return
            for i in range(len(right)):
                cur = int(right[:i+1])
                if i == 0 or (i > 0 and right[0] != '0'):
                    dfs(exp+'+'+right[:i+1], res_of_exp+int(cur), right[i+1:], cur)
                    dfs(exp+'-'+right[:i+1], res_of_exp-int(cur), right[i+1:], -cur)
                    dfs(exp+'*'+right[:i+1], res_of_exp-last+last*int(cur), right[i+1:], last*cur)
        for i in range(len(num)):
            if i == 0 or (i > 0 and num[0] != '0'):
                dfs(num[:i+1], int(num[:i+1]), num[i+1:], int(num[:i+1]))
        return ret




def main():
    s = Solution()
    print(s.addOperators( num = "123", target = 6))
    print(s.addOperators(num = "00", target = 0))
    print(s.addOperators('105', 5))
    print(s.addOperators("1000000009",9))
    print(s.addOperators('123456789', 45))


if __name__ == "__main__":
    main()
