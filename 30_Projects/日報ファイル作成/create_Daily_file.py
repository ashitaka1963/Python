import os
import datetime

def connect_str(base_str, add_str):
    base_str += add_str
    return base_str

WEEKDAY = ['月','火','水','木','金','土','日']
base_str = ''

# 現在日付を取得
today = datetime.date.today()
day = WEEKDAY[today.weekday()]

file_name = today.strftime('%Y%m%d')
h1 = '# ' + today.strftime(f'%Y年%m月%d日（{day}） 日報')
h2_1 = '## AtCoder Beginner Contest全問解いてみたチャレンジ'
h2_2 = '## 今日の学び'

# 本文
base_str = connect_str(base_str, h1)
base_str = connect_str(base_str, '\n\n')
base_str = connect_str(base_str, h2_1)
base_str = connect_str(base_str, '\n\n')
base_str = connect_str(base_str, h2_2)
base_str = connect_str(base_str, '\n\n')
base_str = connect_str(base_str, '<!-- more -->')

# 出力ファイルのパス設定
path = '.\\' +file_name + '.md'

# 書き出し
with open(path, mode='w', encoding='utf-8') as f:
    f.write(base_str)

