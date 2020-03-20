# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s

        flag = numRows - 2
        part_list = []

        cur = 0
        # print("flag: ", flag)
        while cur < len(s):
            buffer = s[cur:cur+numRows]
            cur += numRows
            # print(buffer, cur)
            part_list.append(buffer)
            try:
                for i in range(flag):
                        buffer = " "*(flag- i) + s[cur]
                        cur += 1
                        buffer += " "*(numRows-len(buffer))
                        part_list.append(buffer)
                        # print(buffer)
            except:
                pass


        ret = ""
        for i in range(numRows):
            for part in part_list:
                try:
                    if part[i] != " ":
                        ret += part[i]
                except:
                    pass

        print (ret)
        return ret

    def convert_2(self, s, numRows):
        flag = 0
        interval = 2*numRows-2
        ret = ""
        for i in range(numRows):
            for j in range(int(len(s)/(2*numRows-2))+1):

                try:
                    ret += s[i+interval*j]
                    if flag != 0 and i != numRows-1:
                        ret += s[interval*(j+1) - i]
                except:
                    pass
            flag+=1
        print(ret)
        return ret





def main():
    s = Solution()
    s.convert_2("LEETCODEISHIRING", 4)


if __name__ == "__main__":
    main()
