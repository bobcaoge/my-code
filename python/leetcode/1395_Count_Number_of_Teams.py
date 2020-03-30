# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        smaller_dp = [0]*len(rating)
        bigger_dp = [0]*len(rating)
        r_smaller_dp = [0]*len(rating)
        r_bigger_dp = [0]*len(rating)
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    bigger_dp[i] += 1
                    smaller_dp[j] += 1
                if rating[i] > rating[j]:
                    r_smaller_dp[i] += 1
                    r_bigger_dp[j] += 1
        ret = 0
        for i in range(len(rating)):
            ret += smaller_dp[i]*bigger_dp[i]
            ret += r_smaller_dp[i]*r_bigger_dp[i]
        return ret




def main():
    s = Solution()
    print(s.numTeams([2,5,3,4,1]))


if __name__ == "__main__":
    main()
