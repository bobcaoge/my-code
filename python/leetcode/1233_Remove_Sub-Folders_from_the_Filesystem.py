# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folders = set()
        folder.sort()
        ret = []
        for cur_folder in folder:
            names = cur_folder.split("/")
            for j in range(1, len(names)):
                if "/".join(names[:j]) in folders:
                    break
            else:
                ret.append(cur_folder)
            folders.add(cur_folder)
        return ret

def main():
    s = Solution()
    print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(s.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
    print(s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))


if __name__ == "__main__":
    main()
