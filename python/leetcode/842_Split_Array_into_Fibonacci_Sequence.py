# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    flag = False
    ret = []
    def recursion(self, s, pos, nums):
        if self.flag or nums and nums[-1] > 2**31-1:
            return
        if pos == len(s) and len(nums) >= 3:
            self.flag = True
            self.ret = [x for x in nums]
            return
        if len(nums) in {0, 1}:
            for i in range(pos, len(s)):

                nums.append(int(s[pos:i+1]))
                self.recursion(s, i+1, nums)
                nums.pop()
                if s[pos] == "0":
                    break
        else:
            next_num = nums[-1] + nums[-2]
            length = len(str(next_num))
            if s[pos:pos+length] == str(next_num):
                nums.append(next_num)
                pos += length
                self.recursion(s, pos, nums)
                nums.pop()

    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        self.flag = False
        self.ret = []
        self.recursion(S, 0, [])
        # if self.ret:
        #     print([self.ret[i]+self.ret[i+1] for  i in range(len(self.ret)-1)])
        #     print(self.ret[2:])
        #     print("".join([str(x) for x in self.ret]) == S)
        return self.ret if self.ret else []


def main():
    s = Solution()
    print(s.splitIntoFibonacci("1235"))
    print(s.splitIntoFibonacci("123456579"))
    print(s.splitIntoFibonacci("11235813"))
    print(s.splitIntoFibonacci("1101111"))
    print(s.splitIntoFibonacci("1101122"))
    print(s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))


if __name__ == "__main__":
    main()
