# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        ret = 1<<30
        s = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                s.add(fronts[i])

        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                if fronts[i] not in s:
                    ret = min(ret, fronts[i])
                if backs[i] not in s:
                    ret = min(ret, backs[i])
        return ret if ret != (1<<30) else 0


def main():
    s = Solution()
    print(s.flipgame(fronts = [1,2,4,4,7], backs = [1,3,4,1,3]))


if __name__ == "__main__":
    main()
