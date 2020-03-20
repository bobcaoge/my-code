# /usr/bin/python3.6
# -*- coding:utf-8 -*-


def store(d):
    """
    :type d:dict
    :rtype: str
    """
    ret = ""
    for key, value in d.items():
        length_key = len(key)
        length_value = len(value)
        ret += "{0} {1} {2}={3};".format(length_key, length_value,key, value)
    return ret[:-1]


def load(text):
    """
    :type text: str
    :rtype: dict
    """
    m = {}
    while text:
        length_of_key = ""
        length_of_value = ""
        key_flag = True
        index = 0
        for c in text:
            if c != " ":
                if key_flag:
                    length_of_key += c
                else:
                    length_of_value += c
            else:
                if key_flag:
                    key_flag = False
                else:
                    break
            index += 1
        length_of_key = int(length_of_key)
        length_of_value = int(length_of_value)
        # print(index)
        index += 1
        key = text[index:index+length_of_key]
        value = text[index+length_of_key+1:index+length_of_key+1+length_of_value]
        # print(index)
        text = text[4+length_of_value+length_of_key+len(str(length_of_key))+len(str(length_of_value)):]
        # print(text)
        m[key] = value
    return m
def load1(text):
    """
    :type text: str
    :rtype: dict
    """
    m = {}
    length_of_key = ""
    length_of_value = ""
    key_flag = True
    index = 0
    try:
        length = 0
        while index < len(text):
            c = text[index]
            if c != " ":
                if key_flag:
                    length_of_key += c
                else:
                    length_of_value += c
            else:
                if key_flag:
                    key_flag = False
                else:
                    index += 1
                    # print(length_of_key, length_of_value)
                    length_of_key = int(length_of_key)
                    length_of_value = int(length_of_value)
                    # print(index)
                    key = text[index:index+length_of_key]
                    value = text[index+length_of_key+1:index+length_of_key+1+length_of_value]
                    # print(index)
                    if length == 0:
                        index = 4+length_of_value+length_of_key+len(str(length_of_key))+len(str(length_of_value))-1
                    # else:
                    #     index =
                    print(text[index+1:], "===")
                    print(index)
                    m[key] = value
                    length_of_key = ""
                    length_of_value = ""
                    key_flag = True
                    # break
            index += 1
    except:
        pass
    return m
def main():
    m = {"":"", "hello":"word", "\n":"\n"}
    s = store(m)
    print(s)
    rm = load(s)
    print(rm)


if __name__ == "__main__":
    main()
