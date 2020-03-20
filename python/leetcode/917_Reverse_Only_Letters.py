# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = [c for c in S]
        start = 0
        end = len(S)-1
        while start < end:
            if 'a'<= S[start].lower()<= 'z'  and  'a'<= S[end].lower()<= 'z':
                S[start], S[end] = S[end] , S[start]
                start += 1
                end -= 1
            if not 'a'<= S[start].lower()<= 'z':
                start += 1
            if not 'a'<= S[end].lower()<= 'z':
                end -= 1
        return "".join(S)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
