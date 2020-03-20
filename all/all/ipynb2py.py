import os


def get_file_paths_from_dir(path):
    """
    获取path路径下所有文件的绝对路径
    :param path:
    :return:
    """
    # print(path)
    file_path_list = []
    if not os.path.isdir(path):
        file_path_list.append(path)
        return
    for root, dirs, files in os.walk(path):
        for f in files:
            file_path_list.append(root+'/'+f)
        for d in dirs:
            get_file_paths_from_dir(root+'/'+d)
    return file_path_list


def remove_old_files(remove_path_list, old_file_end):
    """
    删除以old_file_end结尾的文件
    :param remove_path_list:
    :param old_file_end:
    :return:
    """
    for file_path in remove_path_list:
        if file_path.endswith(old_file_end):
            try:
                print("正在删除文件:" + file_path)
                os.remove(file_path)
                print("成功删除文件:"+file_path)
            except:
                print("文件找不到")


def convert(path, remove_old_files_flag = False):
    """
    将ipynb文件转换成py文件
    :param path:
    :param remove_old_files_flag: False 不删除ipynb文件， True 删除ipynb文件
    :return:
    """
    path_front = " jupyter nbconvert --to script "
    path_list = get_file_paths_from_dir(path)
    remove_path_list = []

    for ipynb_file_path in path_list:
        if ipynb_file_path.endswith("ipynb"):
            cmd = path_front + "\"" + ipynb_file_path + "\""
            to_convert_file_path= ipynb_file_path.replace("ipynb", "py")
            # print(to_convert_file_path+"+++++++++++++")
            if not os.path.exists(to_convert_file_path):
                print("正在将ipynb转换为py文件")
                os.system(cmd)
                print("转换完成")
            else:
                print(to_convert_file_path + "已经存在")
            if remove_old_files_flag:
                remove_path_list.append(ipynb_file_path)
    for remove_path in remove_path_list:
        print(remove_path)
    if remove_old_files_flag:
        remove_old_files(remove_path_list, "ipynb")


if __name__ == '__main__':
    path = "C:/Users/bobcao/Desktop/tensorflow代码"
    # path = input("请输入路径\n default ./\n")
    convert(path, True)
    # path_list = get_file_paths_from_dir(path)
    # for p in path_list:
    #     print(p)
    # remove_old_files(path_list, "py")



