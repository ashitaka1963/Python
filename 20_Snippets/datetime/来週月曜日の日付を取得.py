import datetime

def get_next_target_date(date, target_week):
    week = ['月','火','水','木','金','土','日']

    # 曜日を数値型で取得
    weekday = date.weekday()
    # dateから指定した曜日までの加算日数を計算
    add_days = 7 - weekday + week.index(target_week)
    # dateに加算
    next_target_date = date + datetime.timedelta(days = add_days)

    return next_target_date


# 現在の日付を取得する。
today = datetime.date.today()
print(today) # 2020-04-13

# 指定した曜日の来週の日付を取得する。
next_date = get_next_target_date(today, '水')
print(next_date) # 2020-04-21

