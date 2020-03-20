# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        record = num
        num = [x for x in str(num)]
        arr = [""]*len(num)
        max_num = num[-1]
        for i in range(len(num)-2, -1, -1):
            max_num = max(max_num, num[i])
            arr[i] = max_num
        for i in range(len(num)):
            if num[i] == arr[i-1]:
                continue
            pos = i
            for k in range(i, len(num)):
                if num[k] >= num[pos]:
                    pos = num
            num[i], num[pos] = num[pos], num[i]
            return int("".join(num))
        return record



def main():
    s = Solution()
    print(s.maximumSwap(1239))
    print(s.maximumSwap(98368))
    print(s.maximumSwap(1991))


if __name__ == "__main__":
    main()
