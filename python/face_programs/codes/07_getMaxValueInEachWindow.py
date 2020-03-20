# /usr/bin/python3.6
# -*- coding:utf-8 -*-


def get_the_max_value_of_list(data_list, start=0, end=None):
    if end is None:
        end = len(data_list)
    max_value = data_list[start]
    for data in data_list[start:end]:
        if max_value < data:
            max_value = data
    return max_value


def get_max_values_of_list(data_list, data_length, window_length):
    max_value = []
    max_value_of_before = 0
    for moving_step in range(data_length-window_length+1):
        if max_value.__len__() == 0:
            max_value_of_before = get_the_max_value_of_list(data_list, end=window_length)
            max_value.append(max_value_of_before)
        else:
            # print(data_list[moving_step], max_value_of_before, data_list[window_length+moving_step-1] )
            if max_value_of_before != data_list[moving_step-1] and max_value_of_before > data_list[window_length+moving_step-1]:

                max_value.append(max_value_of_before)
            else:
                max_value_of_before = get_the_max_value_of_list(data_list, start=moving_step, end=window_length+moving_step)
                max_value.append(max_value_of_before)
        print(max_value)
    return max_value


def main():
    data_list = [4, 3, 5, 4, 3, 3, 6, 7]
    ret = get_max_values_of_list(data_list, data_length=8, window_length=3)
    print(ret)


if __name__ == '__main__':
    main()






