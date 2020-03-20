# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def calc(self, num1, num2, operator):
        """
        :str num1:
        :str num2:
        :str operator:
        :rtype: str
        """
        num2 = int(num2)*1.0
        num1 = int(num1)
        if operator == "+":
            return str(int(num1+num2))
        elif operator == "*":
            return str(int(num1*num2))
        elif operator == "/":
            return str(int(num1/num2))
        elif operator == "-":
            return str(int(num1-num2))

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/",]:
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calc(num1, num2, token))
                # stack.append(str(int(eval(num1+"*1.0"+token+num2))))
        return int(stack[-1])





def main():
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

if __name__ == "__main__":
    main()
