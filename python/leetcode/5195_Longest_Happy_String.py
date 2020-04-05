# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        def valid(i, c):
            if i-1 >= 0 and i-2>= 0 and ret[i-1]==ret[i-2] == c:
                return False
            if i >= 0 and i+1 < len(ret) and ret[i+1] == ret[i] == c:
                return False
            if i-1 >= 0 and ret[i-1] == ret[i] == c:
                return False
            return True
        info = sorted([[a, 'a'],[b, 'b'],[c, 'c']])
        ret = [info[-1][1]]
        info[-1][0] -= 1
        while True:
            count = 0
            for i, (num, c) in enumerate(info):
                if num <= 0:
                    count+=1
                    continue
                for j in range(len(ret)):
                    if valid(j, c):
                        ret.insert(j, c)
                        info[i][0] -= 1
                        break
                else:
                    count += 1
            if count == 3: break
            # print("".join(ret))
        return "".join(ret)


def main():
    s = Solution()
    print(s.longestDiverseString(1,2,8))
    # print(s.longestDiverseString(4,4,4))
    # print(s.longestDiverseString(0,11,12))


if __name__ == "__main__":
    main()
