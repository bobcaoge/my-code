# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        source = "\n".join(source)
        ret = ""
        flag_of_block = False
        flag_of_row = False
        s = {"/", "*"}
        pos = -1
        i = 0
        while i < len(source):
            c = source[i]
            if not flag_of_block and not flag_of_row:
                if c not in s:
                    ret += c
                else:
                    if i == 0:
                        ret += "c"
                    else:
                        if c == "/" and source[i-1] == "/":
                            flag_of_row = True
                            ret = ret[:-1]
                            i += 1
                        elif c == "*" and source[i-1] == "/":
                            flag_of_block = True
                            ret = ret[:-1]
                            i+=1
                        else:
                            ret += c
            elif flag_of_block and not flag_of_row:
                if c == "/" and source[i-1] == "*":
                    flag_of_block = False
                    if i < len(source)-1:
                        ret += source[i+1]
                        i += 1
            elif not flag_of_block and flag_of_row:
                if c == "\n":
                    flag_of_row = False
                    ret += c
                    if i < len(source)-1:
                        ret += source[i+1]
                        i += 1
            i += 1

        res = []
        for line in ret.split("\n"):
            if line:
                res.append(line)
        return res




def main():
    s = Solution()
    # print(s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
    # print(s.removeComments(["main() {", "   func(1);", "   /** / more comments here", "   float f = 2.0", "   f += f;", "   cout << f; */", "}"]))
    # print(s.removeComments(["main() {", "  Node* p;", "  /* declare a Node", "  /*float f = 2.0", "   p->val = f;", "   /**/", "   p->val = 1;", "   //*/ cout << success;*/", "}", " "]))
    print(s.removeComments(["a/*/b//*c","blank","d/*/e*//f"]))

if __name__ == "__main__":
    main()
