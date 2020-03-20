# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    def step(self, n):
        ret = 0
        while n != 0:

            ret += (n%10)**2
            n = int(n/10)
        return ret

    def isHappy(self, n: 'int') -> 'bool':
        buffer = self.step(n)
        # check = [n, buffer]
        slow = n
        fast = self.step(slow)
        fast = self.step(fast)
        while slow != fast:

            slow = self.step(slow)
            fast = self.step(fast)
            fast = self.step(fast)
        if fast == 1:
            return True
        return False



def main():
    s = Solution()


if __name__ == "__main__":
    main()
