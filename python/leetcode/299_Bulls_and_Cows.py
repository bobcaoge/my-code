# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        secret_wrong = ""
        guess_wrong = {}
        for i, num in enumerate(secret):
            if num == guess[i]:
                bull += 1
            else:
                secret_wrong += num
                guess_wrong[guess[i]] = guess_wrong.get(guess[i], 0) +1
        for c in secret_wrong:
            if guess_wrong.get(c, 0) > 0:
                cow += 1
                guess_wrong[c] -= 1
        return "{0}A{1}B".format(bull, cow)


def main():
    s = Solution()
    print(s.getHint("1807", "7810"))
    print(s.getHint("1123", "0111"))
    print(s.getHint("", ""))


if __name__ == "__main__":
    main()
