# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == "#":
            return True
        if preorder == "":
            return False
        i = 0
        preorder = preorder.split(",")
        length = len(preorder)
        stack = [preorder[i]]
        i += 1

        while i < length and stack:
            cur = preorder[i]
            if stack[-1] != "#":
                stack.append(cur)
            else:
                if cur != "#":
                    stack.append(cur)
                else:
                    while stack and stack[-1] == "#":
                        try:
                            stack.pop()
                            stack.pop()
                        except:
                            return False
                    stack.append("#")
            i += 1
        if i == length and stack == ["#"]:
            return True
        return False




def main():
    s = Solution()
    print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(s.isValidSerialization("9,#,#,1"))
if __name__ == "__main__":
    main()
