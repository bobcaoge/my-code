# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def buffer( candidates, target, i, ans,  ret):
            # print(ans)
            # diff = target - sum_of_ans
            if target == 0:
                ret.append(ans)
            elif target < 0:
                return
            length = len(candidates)
            for index in range(i,length):
                buffer(candidates, target-candidates[index], index, ans + [candidates[index]], ret)
        ret = []
        candidates.sort()
        buffer(candidates, target, 0, [], ret)
        return ret





def main():
    s = Solution()
    print(s.combinationSum(candidates = [2,3,5,7], target = 7))
    print(s.combinationSum([2,3,5], target = 8,))


if __name__ == "__main__":
    main()
