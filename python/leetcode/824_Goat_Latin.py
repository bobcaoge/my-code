# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ret = ""
        cur = -1
        word_num = 1
        character_set = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        character_set = set(character_set)
        S += " "
        for index, s in enumerate(S):
            if s == " ":
                if S[cur+1] in character_set:
                    ret += S[cur+1:index]+"ma"+'a'*word_num
                else:
                    ret += S[cur+2:index]+S[cur+1]+"ma"+'a'*word_num
                ret += " "
                cur = index
                word_num += 1
        return ret[:-1]


def main():
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))



if __name__ == "__main__":
    main()
