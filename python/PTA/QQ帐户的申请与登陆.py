#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
class Qq(object):
    def __init__(self):
        self.data = {}
    def sign_in(self, username, password):
        if username in self.data:
            if self.data[username] == password:
                return "Login: OK"
            else:
                return "ERROR: Wrong PW"
        return "ERROR: Not Exist"
    def valid(self, username, password):
        if 1000 < username < 10**10-1 and 6<= len(password) <= 16:
            return True
        return False
    def sign_up(self, username, password):
        # if self.valid(username, password):
            if username not in self.data:
                self.data[username] = password
                return "New: OK"
            return "ERROR: Exist"

def main():
    qq = Qq()
    k = int(input())
    for i in range(k):
        z, username, password = [x for x in input().split(' ')]
        username = int(username)
        if z == 'N':
            print(qq.sign_up(username, password))
        elif z == 'L':
            print(qq.sign_in(username, password))




if __name__ == "__main__":
    main()