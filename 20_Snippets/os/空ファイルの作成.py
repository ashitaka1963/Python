import os
import pathlib

# カレントディレクトリに空ファイルを作成する。

def create_task_file(base_path, file_name):
    path =  base_path + "\\" + file_name
    if not os.path.exists(path):
        p_empty = pathlib.Path(path)
        p_empty.touch()

path = os.getcwd()
file_name = "test.py"
create_task_file(path, file_name)