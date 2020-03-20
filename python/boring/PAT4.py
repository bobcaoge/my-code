# /usr/bin/python3.6
# -*- coding:utf-8 -*-


def main():
    s = raw_input()
    # print(s)
    numbers = [0] * (len(s))
    carry = 0
    for i, c in enumerate(s[::-1]):
        cur = int(c) * 2 + carry
        numbers[i] = str(cur % 10)
        carry = cur / 10
    if carry > 0:
        print "No"
        result = "".join(numbers)[::-1]
        print(str(carry) + result)
    else:
        result = "".join(numbers)[::-1]
        if sorted(s) == sorted(result):
            print("Yes")
            print(result)
        else:
            print("No")

            print(result)


if __name__ == "__main__":
    main()
