# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        i = 0
        j = len(tokens)-1
        score = 0
        ret = 0
        while i <= j:
            if P >= tokens[i]:
                score += 1
                ret = max(ret, score)
                P -= tokens[i]
                i += 1
            else:
                if score > 0:
                    score -= 1
                    P += tokens[j]
                    j -= 1
                else:
                    return ret
        return ret


def main():
    s = Solution()
    print(s.bagOfTokensScore(tokens = [100,200,300,400], P = 200))
    print(s.bagOfTokensScore([100,200], P = 150))


if __name__ == "__main__":
    main()
