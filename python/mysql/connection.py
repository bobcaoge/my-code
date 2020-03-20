#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
import pymysql
import random
def main():
    conn = pymysql.connect(host="192.168.1.177", port=3306, user="root", passwd="caoge", db="python", charset="utf8")
    cursor = conn.cursor()
    # for i in range(11):
    #     sql = "insert into students(name, gender) values('{0}', {1});".\
    #         format(str(chr(i+ord('a')))*3, random.randint(0, 1))
    #     cursor.execute(sql)
    # for i in range(11):
    #     sql = "insert into scores(stuid, subid, scores) values({0}, {1}, {2})"\
    #         .format(i+6, random.randint(1, 3), random.randint(70, 90))
    #     cursor.execute(sql)
    cursor.execute("select * from students")
    conn.commit()
    cursor.close()
    conn.close()
    pass


if __name__ == "__main__":
    main()