# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if set(name) != set(typed):
            return False
        index_of_name = 0
        length = len(name)

        for index, c in enumerate(typed):
            if name[index_of_name] == c:
                index_of_name += 1
                if index_of_name == length:
                    return True
            else:
                if index != 0 and typed[index] != typed[index-1]:
                    return False
        return index_of_name == length


def main():
    s = Solution()
    print(s.isLongPressedName("saeed", "ssaaedd"))


if __name__ == "__main__":
    main()
