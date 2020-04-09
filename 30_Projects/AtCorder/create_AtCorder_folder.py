import os
import pathlib


def make_base_dir(base_path, dir_name):
    path =  base_path + "\\" + dir_name
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def zero_padding(question_num, digits):
    file_name = str(question_num).zfill(digits)
    return file_name


def create_task_file(base_path, dir_name, task):
    path =  base_path + "\\" + dir_name +"_" + task + extension
    if not os.path.exists(path):
        p_empty = pathlib.Path(path)
        p_empty.touch()

def make_contests_times_dir(base_path, contest_name, question_num):

    contests_times = zero_padding(question_num, digits)
    dir_name =  contest_name + contests_times
    path =  base_path + "\\" + dir_name

    if not os.path.exists(path):
        os.mkdir(path)

    tasks = ['A', 'B', 'C', 'D', 'E', 'F']

    # AtCoder Beginner Contestは第125回までA~D問題のため。
    if (contest_name == "ABC" and question_num <=125) or contest_name == "ARC":
        tasks = ['A', 'B', 'C', 'D']

    for task in tasks:
        create_task_file(path, dir_name, task)


def make_contests_dir(base_path, contest_name, contest_nums):
    path =  base_path + "\\" + contest_name
    if not os.path.exists(path):
        os.mkdir(path)

    for question_num in range(contest_nums):
        make_contests_times_dir(path, contest_name , question_num + 1)


# main
path = os.getcwd()
path = make_base_dir(path, "AtCorder")

digits = 3
extension = ".py"

# =================== AtCoder Beginner Contest ===================
contest_nums = 160
make_contests_dir(path, "ABC", contest_nums)

# =================== AtCoder Regular Contest ===================
# contest_nums = 103
# make_contests_dir(path, "ARC", contest_nums, extension)

input()
