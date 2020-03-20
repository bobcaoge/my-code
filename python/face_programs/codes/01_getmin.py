# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class NoneOfStack(Exception):
    info = "stack is empty"


class SpecialStack(object):
    def __init__(self):
        self.new_stack = []
        self.min_stack = []
        self.length_of_min_stack = 0
        self.length_of_new_stack = 0

    def pop(self):
        value = self.new_stack.pop()
        self.length_of_new_stack -= 1
        if value > self.min_stack[-1]:
            return value
        else:
            self.length_of_min_stack -= 1
            return self.min_stack.pop()

    def push(self, data):
        self.new_stack.append(data)
        self.length_of_new_stack += 1
        if self.length_of_min_stack == 0:
            self.min_stack.append(data)
            self.length_of_min_stack += 1
        else:
            min_data = self.get_min()
            if data <= min_data:
                self.min_stack.append(data)
                self.length_of_min_stack += 1

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            raise NoneOfStack()

    def push_many(self, datas):
        for data in datas:
            self.push(data)
            # print(self.get_min())


def main():
    st = SpecialStack()
    st.push_many([3, 4, 5, 1, 2, 1])
    for _ in range(st.length_of_new_stack):
        try:
            print(st.get_min())
        except NoneOfStack:
            print(NoneOfStack.info)
        print(st.min_stack, st.new_stack)
        st.pop()

    print(st.min_stack, st.new_stack)


if __name__ == '__main__':
    main()
