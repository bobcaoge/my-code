# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def manage(self, s):
        length = len(s)
        for i in range(length):
            a = s[:i+1]*2
            b = s[:2*(i+1)]
            if s[:i+1]*2 == s[:2*(i+1)] and s[i] != "0":
                return "("+s[:i+1]+")"

    def get_float(self, num2, num1):
        i = 0
        ret_int = ""
        ret_float = ""
        flag = True
        minus_flag = True if num1 < 0 < num2 or num2 < 0 < num1 else False
        num1 = abs(num1)
        num2 = abs(num2)

        while i < 10000 and num2 != 0:
            buff = num2 / num1
            if flag and buff == 0:
                flag = False
            if flag:
                ret_int += str(buff)
                num2 -= buff * num1
            else:
                num2 *= 10
                buff = num2 / num1
                ret_float += str(buff)
                num2 -= buff * num1
            i+=1
        if not ret_int:
            ret_int = "0"
        if minus_flag:
            ret_int = "-"+ret_int
        return ret_int+"."+ret_float if ret_float else ret_int

    def fractionToDecimal1(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        nums_of_two = 0
        nums_of_five = 0
        result_str = self.get_float(numerator, denominator)
        # result_str = str(numerator*1.0/denominator*1.0)[:-1]
        result = numerator*1.0/denominator*1.0
        while denominator != 0:
            if denominator % 2 == 0:
                nums_of_two += 1
                denominator /= 2
            else:
                break
        while denominator != 0:
            if denominator % 5 == 0:
                nums_of_five += 1
                denominator /= 5
            else:
                break
        # print(result_str)
        if result_str.__len__() < 100:
            if result == int(result):
                return str(int(result))
            return result_str
        else:
            index_of_dot = result_str.index(".")
            if nums_of_five == nums_of_two == 0:
                circle_part = self.manage(result_str[index_of_dot+1:])
                return result_str[:index_of_dot+1] + circle_part
            else:
                not_circle_part_after_dot = max(nums_of_two, nums_of_five)
                circle_part = self.manage(result_str[index_of_dot+1+not_circle_part_after_dot:])
                return result_str[:index_of_dot+1+not_circle_part_after_dot] + circle_part

    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        nums_of_two = 0
        nums_of_five = 0
        num2 = numerator
        num1 = denominator
        while denominator != 0:
            if denominator % 2 == 0:
                nums_of_two += 1
                denominator /= 2
            else:
                break
        while denominator != 0:
            if denominator % 5 == 0:
                nums_of_five += 1
                denominator /= 5
            else:
                break

        not_circle_part_after_dot = max(nums_of_two, nums_of_five)
        numerator, denominator = num2, num1
        minus_flag = True if denominator < 0 < numerator or numerator < 0 < denominator else False
        denominator = abs(denominator)
        numerator = abs(numerator)

        ret_int = ""
        # calculate the int part
        while numerator != 0:
            buff = numerator / denominator
            if buff == 0:
                break
            ret_int += str(buff)
            numerator -= buff * denominator
        # calculate the not circle part after dot
        not_circle_part = ""
        while not_circle_part_after_dot != 0 and numerator != 0:
            numerator *= 10
            buff = numerator / denominator
            not_circle_part += str(buff)
            numerator -= buff * denominator
            not_circle_part_after_dot -= 1
        # calculate the circle part
        circle_part = ""
        length = 1
        while numerator != 0:
            numerator *= 10
            buff = numerator / denominator
            circle_part += str(buff)
            if buff != 0 and length % 2 == 0 and circle_part[:length/2]*2 == circle_part:
                circle_part = circle_part[:length/2]
                break
            length += 1
            numerator -= denominator*buff

        if not ret_int:
            ret_int = "0"
        if minus_flag:
            ret_int = "-"+ret_int
        if numerator == 0:
            return ret_int + "." + not_circle_part if not_circle_part else ret_int
        ret = ret_int + "." + not_circle_part
        if circle_part:
            return ret+"("+circle_part+")"
        else:
            return ret


def main():
    s = Solution()
    print(s.fractionToDecimal(-1, 2**32*3))
    print(s.fractionToDecimal(-1, 2**32))
    print(s.fractionToDecimal(1,2))
    print(s.fractionToDecimal(2,1))
    print(s.fractionToDecimal(1,3))
    print(s.fractionToDecimal(1,30))
    print(s.fractionToDecimal(2,3))
    print(s.fractionToDecimal(-22, 2))
    print(s.fractionToDecimal(4, 333))
    print(s.fractionToDecimal(1, 333))
    print(s.fractionToDecimal(-2147483648, -1999))



if __name__ == "__main__":
    main()
