# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        dp_L_from_left_to_right = [0]*len(A)
        dp_M_from_right_to_left= [0]*len(A)

        dp_L_from_right_to_left= [0]*len(A)
        dp_M_from_left_to_right = [0]*len(A)

        cur_L = 0
        cur_right = 0
        for i, num in enumerate(A):
            cur_L += num
            cur_right += num
            if i + 1 >= L:
                dp_L_from_left_to_right[i] = max(dp_L_from_left_to_right[i-1] if i-1 >= 0 else 0, cur_L)
                cur_L -= A[i-L+1]
            if i + 1 >= M:
                dp_M_from_left_to_right[i] = max(dp_M_from_left_to_right[i-1] if i-1 >= 0 else 0, cur_right)
                cur_right -= A[i-M+1]

        cur_L = 0
        cur_right = 0
        for i in range(len(A)-1, -1, -1):
            cur_L += A[i]
            cur_right += A[i]
            if len(A) - i >= L:
                dp_L_from_right_to_left[i] = max(dp_L_from_right_to_left[i+1] if i+1 < len(A) else 0, cur_L)
                cur_L -= A[i+L-1]
            if len(A) - i >= M:
                dp_M_from_right_to_left[i] = max(dp_M_from_right_to_left[i+1] if i+1 < len(A) else 0, cur_right)
                cur_right -= A[i+M-1]
        ret = 0
        for i in range(len(A)-1):
            ret = max(ret, dp_L_from_left_to_right[i]+dp_M_from_right_to_left[i+1])
            ret = max(ret, dp_M_from_left_to_right[i]+dp_L_from_right_to_left[i+1])
        return ret








def main():
    s = Solution()
    print(s.maxSumTwoNoOverlap(A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2))
    print(s.maxSumTwoNoOverlap( A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2))
    print(s.maxSumTwoNoOverlap(A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3))


if __name__ == "__main__":
    main()
