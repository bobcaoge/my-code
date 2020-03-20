# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        start = 0
        end = 0
        infix = []
        while end < len(s):
            if "0" > s[end] or s[end] > "9":
                infix.append(s[start:end])
                infix.append(s[end])
                start = end+1
            end += 1
        infix.append(s[start:end])
        print(infix)
        postfix = self.transform_infix_to_postfix(infix)
        print(postfix)
        return self.calculate_from_postfix(postfix)

    def calculate_the_result_of_two_num(self,num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return num1 / num2

    def calculate_from_postfix(self, postfix):
        stack = []
        for s in postfix:
            if s not in {"+", "-", "*", "/"}:
                stack.append(s)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calculate_the_result_of_two_num(num1, num2, s))
        return stack[-1]

    def transform_infix_to_postfix(self, infix):
        postfix = []
        stack = []
        priority = {
            "+":1,
            "-":1,
            "*":2,
            "/":2
            }
        for s in infix:
            if s not in {"+", "-", "*", "/"}:
                postfix.append(int(s))
            else:
                while stack and priority[stack[-1]] >= priority[s]:
                    postfix.append(stack.pop())
                stack.append(s)
        while stack:
            postfix.append(stack.pop())
        return postfix


    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s.replace(" ", ""))


def main():
    s = Solution()
    print(s.calculate("2*9+6/3-5+4"))


if __name__ == "__main__":
    main()
