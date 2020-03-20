# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        distance = abs(target[0])+abs(target[1])
        for x, y in ghosts:
            if distance >= abs(x- target[0])+abs(y-target[1]):
                return False
        return True



def main():
    s = Solution()
    print(s.escapeGhosts([[1,0],[0,3]],[0,1]))
    print(s.escapeGhosts(ghosts = [[1, 0]], target = [2, 0]))


if __name__ == "__main__":
    main()
