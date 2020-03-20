# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_higher = [-1]*len(height)
        stack = []
        for i in range(len(height)-1, -1, -1):
            while stack and  height[i] >= height[stack[-1]]:
                left_higher[stack[-1]] = i
                stack.pop()
            stack.append(i)
        index_of_cur_max = 0
        dp = [0]*len(height)
        for i in range(1, len(height)):
            if height[i] > height[i-1]:
                if height[i] >= height[index_of_cur_max]:
                    dp[i] = dp[index_of_cur_max] + (i-index_of_cur_max-1)*height[index_of_cur_max] - sum(height[index_of_cur_max+1:i])
                else:
                    dp[i] = dp[left_higher[i]] + (i-left_higher[i]-1)*height[i] - sum(height[left_higher[i]+1:i])
            else:
                dp[i] = dp[i-1]
            if height[i] >= height[index_of_cur_max]:
                index_of_cur_max = i
        return dp[-1]



def main():
    s = Solution()
    print(s.trap([3,2,0,2]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


if __name__ == "__main__":
    main()
