import os

# os.path.exists(path)

current_path = os.getcwd()
dir_name = "DirName"
path =  current_path + "\\" + dir_name

# フォルダの存在確認
if not os.path.exists(path):
    # フォルダを作成する。
    os.mkdir(path)
