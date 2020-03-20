# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        num_s = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
                 'Eighteen', 'Nineteen', 'Twenty']
        buff = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        carry = ['', 'Thousand', 'Million', 'Billion']
        def manager(cur_num):
            ret = []
            if cur_num >= 100:
                ret.append(num_s[cur_num//100-1])
                ret.append('Hundred')
            cur_num = cur_num % 100
            if 0 < cur_num <= 20:
                ret.append(num_s[cur_num-1])
            elif cur_num >= 21:
                ret.append(buff[cur_num//10-2])
                if cur_num%10 != 0:
                    ret.append(num_s[cur_num%10 - 1])
            return ret
        i = 0
        res = []
        num = str(num)
        while i < len(num):
            cur_num =int(num[max(len(num)-i-3, 0):len(num)-i])
            if cur_num != 0:
                res = manager(cur_num) + [carry[i//3]] + res
            i += 3
        return ' '.join(res).rstrip(' ')




def main():
    s = Solution()
    print(s.numberToWords(123))
    print(s.numberToWords(123456789))
    print(s.numberToWords(1000001))
    print(s.numberToWords(0))
    print(s.numberToWords(1000))


if __name__ == "__main__":
    main()
