# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {
            5: 0,
            10: 0,
            20: 0
        }
        for bill in bills:
            changes[bill] += 1
            to_change = bill - 5
            while to_change != 0:
                if to_change >= 10 and changes[10] > 0:
                    changes[10] -= 1
                    to_change -= 10
                if to_change >= 5:
                    if changes[5] == 0:
                        return False
                    changes[5] -= 1
                    to_change -= 5
        return True




def main():
    s = Solution()


if __name__ == "__main__":
    main()
