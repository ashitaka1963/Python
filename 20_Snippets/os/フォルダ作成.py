import os

# カレントディレクトリにフォルダ作成

def make_dir(current_path, dir_name):
    path =  current_path + "\\" + dir_name

    # フォルダの存在確認
    if not os.path.exists(path):
        os.mkdir(path)

current_path = os.getcwd()
dir_name = "DirName"
make_dir(current_path, dir_name)