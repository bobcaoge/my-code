# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = set()
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def buffer(candidates, target, i, ans):
            # print(ans)
            if target == 0:
                self.ret.add(tuple(ans))
            elif target < 0:
                return
            for index in range(i,len(candidates)):
                buffer(candidates, target-candidates[index], index+1, [x for x in ans] + [candidates[index]])
        self.ret = set()
        candidates.sort()
        buffer(candidates, target, 0, [])
        return [list(ans) for ans in self.ret]

def main():
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))

if __name__ == "__main__":
    main()
