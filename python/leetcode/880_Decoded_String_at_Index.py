# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        record = [1] # 记录每个位置对应的字符串长度
        for i in range(1, len(S)):
            if S[i].isdigit():
                record.append(record[-1]*int(S[i]))
            else:
                record.append(record[-1]+1)
            if record[-1] >= K:
                break
        # 如果K是当前长度的倍数，那么应是当前字符串的尾字符，
        #       1,如果当前位置是数字，应是上一位置字符串的尾字符，
        #       2,如果不是所求字符即为当前字符
        for i in range(len(record)-1, -1, -1):
            if K >= record[i]:
                K %= record[i]
            if K == 0:
                if S[i].isdigit():
                    continue
                else:
                    return S[i]


def main():
    s = Solution()
    print(s.decodeAtIndex('leet2code3', 8))


if __name__ == "__main__":
    main()
