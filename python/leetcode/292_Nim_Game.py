# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    # def canWinNim(self, n: 'int') -> 'bool':
    #     if n <= 3:
    #         return True
    #     if n == 4:
    #         return False
    #     if n == 5:
    #         return True
    #     flag = True
    #     last = 1
    #     i = 6
    #     while i <= n:
    #         # 胜利维持
    #         if flag:
    #             if last < 3:
    #                 last += 1
    #             else:
    #                 last = 1
    #                 flag = False
    #         # 失败逆转
    #         else:
    #             flag = True
    #             last = 1
    #         i+=1
    #     return flag
    def canWinNim(self, n: 'int') -> 'bool':
        return not n % 4 == 0



def main():
    s = Solution()
    print(s.canWinNim(4))
    print(s.canWinNim(5))
    print(s.canWinNim(6))
    print(s.canWinNim(7))
    print(s.canWinNim(8))


if __name__ == "__main__":
    main()
