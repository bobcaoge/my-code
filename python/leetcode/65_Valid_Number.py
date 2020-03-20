# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isNumber(self, ss):
        """
        :type s: str
        :rtype: bool
        """
        def manager(s, flag):
            if not s:
                return False

            chars = {str(x) for x in range(10)}
            chars.update({".", "-", "+"})
            num = 0
            for c in s:
                if '0'<= c <= '9':
                    num += 1
                if c not in chars:
                    return False
            if num == 0:
                return False
            if s.count("-") + s.count("+") > 1 or s.count("-") > 1 or s.count("+") > 1\
                    or s.find('-') > 0 or s.find('+') > 0 :
                return False
            if s.count('e') > 1 or s.find('e') in{ len(s)-1, 0}:
                return False
            if flag:
                # 后部分不能带点
                if s.count('.') > 0:
                    return False
            else:
                if s.count('.') > 1:
                    return False
            return True

        ss = ss.lstrip(' ').rstrip(' ')
        parts = ss.split('e')
        if len(parts) > 2:
            return False
        if len(parts) == 1:
            return manager(parts[0], False)
        if len(parts) == 2:
            return manager(parts[0], False) and manager(parts[1], True)




def main():
    s = Solution()
    print(s.isNumber('0'))
    print(s.isNumber("1  a"))
    print(s.isNumber("-1"))
    print(s.isNumber("1e1"))
    print(s.isNumber(".1e1"))
    print(s.isNumber("e1"))
    print(s.isNumber("1e.1"))
    print(s.isNumber("--1"))
    print(s.isNumber("-+1"))
    print(s.isNumber("-1e"))
    print(s.isNumber("6e-1"))
    print(s.isNumber("99e2.3"))
    print(s.isNumber("55.3e23"))
    print(s.isNumber('-'))
    print(s.isNumber('.'))
    print(s.isNumber('e'))
    print(s.isNumber('-.'))
    print(s.isNumber('1-'))
    print(s.isNumber(". 1"))


if __name__ == "__main__":
    main()
