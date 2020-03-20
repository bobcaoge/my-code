# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import re

class Solution(object):
    pattern = re.compile(r"\..+")

    def update_path(self, path, ret):
        if self.pattern.findall(path) and len(path) > ret:
            ret = len(path)
        return ret

    def lengthLongestPath(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = []
        old_layer = 0
        last = ""
        i = 0
        ret = 0
        while i < len(s):
            if s[i] not in ["\n", "\t"]:
                last += s[i]
            else:
                i += 1
                cur_layer = 0
                num_of_space = 0
                while s[i] in ["\t", " "] and cur_layer < old_layer+1:
                    if s[i] == "\t":
                        cur_layer += 1
                    if s[i] == " ":
                        num_of_space += 1
                        if num_of_space == 4:
                            cur_layer += 1
                    i += 1
                i -= 1
                if cur_layer == 0:
                    stack.append(last)
                    cur_path = "/".join(stack)
                    ret = self.update_path(cur_path, ret)
                    stack.clear()
                    old_layer = 0
                    last = ""
                    i += 1
                    continue
                if cur_layer > old_layer:
                    stack.append(last)
                    old_layer = cur_layer
                elif cur_layer == old_layer:
                    stack.append(last)
                    cur_path = "/".join(stack)
                    ret = self.update_path(cur_path, ret)
                    stack.pop()
                else:
                    stack.append(last)
                    cur_path = "/".join(stack)
                    ret = self.update_path(cur_path, ret)
                    for j in range(old_layer-cur_layer):
                        stack.pop()
                    stack.pop()
                    old_layer = cur_layer
                last = ""
            i += 1
        stack.append(last)
        cur_path = "/".join(stack)
        ret = self.update_path(cur_path, ret)
        return ret




def main():
    s = Solution()
    print(s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    print(s.lengthLongestPath("a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"))
    print(s.lengthLongestPath("dir\n    file.txt"))
    print(s.lengthLongestPath("file name with  space.txt"))
    print(s.lengthLongestPath("dir\n        file.txt"))
    print(s.lengthLongestPath("skd\n\talskjv\n\t\tlskjf\n\t\t\tklsj.slkj\n\t\tsdlfkj.sdlkjf\n\t\tslkdjf.sdfkj\n\tsldkjf\n\t\tlskdjf\n\t\t\tslkdjf.sldkjf\n\t\t\tslkjf\n\t\t\tsfdklj\n\t\t\tlskjdflk.sdkflj\n\t\t\tsdlkjfl\n\t\t\t\tlskdjf\n\t\t\t\t\tlskdjf.sdlkfj\n\t\t\t\t\tlsdkjf\n\t\t\t\t\t\tsldkfjl.sdlfkj\n\t\t\t\tsldfjlkjd\n\t\t\tsdlfjlk\n\t\t\tlsdkjf\n\t\tlsdkjfl\n\tskdjfl\n\t\tsladkfjlj\n\t\tlskjdflkjsdlfjsldjfljslkjlkjslkjslfjlskjgldfjlkfdjbljdbkjdlkjkasljfklasjdfkljaklwejrkljewkljfslkjflksjfvsafjlgjfljgklsdf.a"))


if __name__ == "__main__":
    main()
