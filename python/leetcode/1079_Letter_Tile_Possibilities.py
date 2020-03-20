# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        cur = set()
        for tile in tiles:
            if not cur:
                cur.add(tile)
            else:
                n = set()
                n.add(tile)
                for sequence in cur:
                    n.update({sequence[:i]+tile+sequence[i:] for i in range(len(sequence)+1)})
                cur.update(n)
        return len(cur)


def main():
    s = Solution()
    print(s.numTilePossibilities("ABCDEFG"))


if __name__ == "__main__":
    main()
