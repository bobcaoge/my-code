# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        m = {0:[],
             1:[],
             2:[]}
        for digit in digits:
            m[digit%3].append(digit)
        last = (m[1].__len__()+2*m[2].__len__())% 3
        m[1].sort(reverse=True)
        m[2].sort(reverse=True)
        if last == 1:
            if len(m[1]) != 0:
                m[1].pop()
            elif len(m[2]) >= 2:
                m[2].pop()
                m[2].pop()
        elif last == 2:
            if len(m[2]) != 0:
                m[2].pop()
            else:
                m[1].pop()
                m[1].pop()
        res = m[0]+m[1]+m[2]
        res.sort(reverse=True)
        ret = "".join([str(x) for x in res])
        buff = ret.lstrip('0')
        if buff:
            return buff
        if ret:
            return '0'



def main():
    s = Solution()
    # print(s.largestMultipleOfThree([8,1,9]))
    print(s.largestMultipleOfThree([8,7,6,1,0]))


if __name__ == "__main__":
    main()
