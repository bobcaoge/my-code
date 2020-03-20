# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        m = collections.Counter(S)
        num = max(x for _, x in m.items())
        if num > len(S)-num+1:
            return ""
        # info = sorted([[c, count] for c, count in m.items()], lambda x, y: True if x[1] < y[1] else False)
        info = sorted([[c, count] for c, count in m.items()])

        ret = ""
        while len(info) > 1:
            buff = []
            for c, count in info:
                ret += c
                if count > 1:
                    buff.append([c, count-1])
            info = buff
        if len(info) == 0:
            return ret
        res = ret
        flag = 0
        if ret[0] != info[0][0]:
            res = info[0][0] + ret
            flag += 1
            info[0][1] -= 1
        for i in range(len(ret)):
            if info[0][1] == 0:
                break
            if i == len(ret)-1 and ret[-1] != info[0][0]:
                res = res + info[0][0]
                info[0][1] -= 1
            else:
                if ret[i] != info[0][0] and ret[i+1] != info[0][0]:
                    res = res[:i+flag+1]+info[0][0]+res[i+flag+1:]
                    flag += 1
                    info[0][1] -= 1
        return res


def main():
    s = Solution()
    # print(s.reorganizeString("aab"))
    # print(s.reorganizeString("vvvol"))
    # print(s.reorganizeString("abcde"))
    print(s.reorganizeString("wfndrin"))


if __name__ == "__main__":
    main()
