# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = [""]*n
        for i in range(1, n+1):
            buffer = ""
            if i % 3 == 0:
                buffer += "Fizz"
            if i % 5 == 0:
                buffer += "Buzz"
            if buffer:
                ret[i-1] = buffer
                # ret.append(buffer)
            else:
                ret[i-1] = str(i)
                # ret.append(str(i))
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
