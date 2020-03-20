#! /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re
import json


def get_type(filename, path):
    """
    根据完整路径path获取filename的文件类型
    如果
    :type filename: str
    :type path: str
    :return:
    """
    if path.endswith(filename):
        return "file"
    return "folder"


def add_path(root, path):
    """
    将完整路径path的信息添加到root数据结构中
    :type path: str
    :type root: dict
    :return:
    """
    url = ""
    path = path.replace("\"", "")
    _ = path.split("/")
    print(path, path.split("/"))
    for name in path.split('/'):
        url += "/"+name
        # print(url)
        for node in root["content"]:
            if node["name"] == name:
                root = node
                break
        else:
            new_node = {
                "name": name,
                "type": get_type(name, path),
                "url": url,
                "content": []
            }
            root["content"].append(new_node)
            root = new_node


def generate_data(s):
    """
    根据字符串s生成相应的数据结构root
    :param s:
    :return:
    """
    pattern = re.compile(r"\[(.*?)\]")
    paths = pattern.findall(s)[0].split(",")
    root = {
                "name": "",
                "type": "",
                "url": "",
                "content": []
            }

    for path in paths:
        add_path(root, path)
    return root


def read_file(filename):
    """
    获取文件filename中的内容
    :param filename:
    :return:
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        return ""


def generate_json(root):
    """
    将字典转换成json
    :type root: dict
    :return:
    """
    # 删除多余的空内容，并将单引号改为双引号
    return json.dumps(root).replace("\"content\": [],", "").replace("\'","\"")


def path2json(path):
    """

    :param path: 路径字符串，包含所有的路径
    :return:
    """
    root = generate_data(path)
    json_data = generate_json(root)
    return json_data


def main():
    path = read_file("../testcase/te1.txt")
    print(path2json(path))




if __name__ == "__main__":
    main()