# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def get_overlapped_length(a, b, c, d):
            if a <= c <= b:
                if d <= b:
                    return d-c
                else:
                    return b-c
            if a <= d <= b:
                return d - a
            if c <= a <= d:
                if b <= d:
                    return b-a
                else:
                    return d-a
            if c <= b <= d:
                return b-c
            return 0

        # def get_area_of_rectangle(a, b, c, d):
        #     return (c-a)*(d-b)
        overlapped_area = get_overlapped_length(A, C, E, G)*get_overlapped_length(B, D, F, H)
        area_of_two_rectangle = (C-A)*(D-B) + (G-E)*(H-F)
        return area_of_two_rectangle-overlapped_area





def main():
    s = Solution()


if __name__ == "__main__":
    main()
