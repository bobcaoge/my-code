# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        length = len(chars)
        if length <= 1:
            return length
        last = 0
        old = chars[0]
        i = 1
        while i < len(chars):
            if old == chars[i]:
                last += 1
                chars[i:i+1] = []
            else:
                old = chars[i]
                if last != 0:
                    s = str(last+1)
                    length_insert = len(s)
                    for index in range(length_insert):
                        chars.insert(i, s[length_insert-index-1])
                    i += length_insert+1
                else:
                    i += 1
                last = 0
        if last != 0:
            s = str(last+1)
            length_insert = len(s)
            for index in range(length_insert):
                chars.insert(i, s[length_insert-index-1])
        return len(chars)



def main():
    s = Solution()
    l = ["a","a","b","b","c","c","c"]
    print(s.compress(l), l)
    l = ["a","b","b","c","c","c"]
    print(s.compress(l), l)
    l = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(s.compress(l), l)
    l = ["a","b","b","b","b","b","b","b","b","b","b","b","b","a","a","a","a","a"]
    print(s.compress(l), l)



if __name__ == "__main__":
    main()
