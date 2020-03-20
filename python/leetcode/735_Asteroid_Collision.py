# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                flag = True
                while stack and stack[-1] > 0 > asteroid:
                    if -asteroid < stack[-1]:
                        flag = False
                        break
                    if -asteroid == stack[-1]:
                        flag = False
                        stack.pop()
                        break
                    if -asteroid > stack[-1]:
                        stack.pop()
                if flag:
                    stack.append(asteroid)
        return stack


def main():
    s = Solution()
    print(s.asteroidCollision([5, 10, -5]))
    print(s.asteroidCollision([8, -8]))
    print(s.asteroidCollision([-8, 8, 3, 7, 5, -7, 8, -9]))


if __name__ == "__main__":
    main()
