# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s_list = str.split(" ")
        if len(pattern) != len(s_list):
            return False
        map_table = {}
        for i in range(len(s_list)):
            a = s_list[i]
            b = pattern[i]
            if not map_table.keys().__contains__(a):
                if map_table.values().__contains__(b):
                    return False
                map_table[a] = b
            else:
                if map_table[a] != b:
                    return False

        print(map_table)
        return True




def main():
    s = Solution()


if __name__ == "__main__":
    main()
