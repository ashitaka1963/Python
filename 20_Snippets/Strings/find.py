# 検索 find

## 見つかった場合はその位置、見つからなった場合は 「-1」 が返る

s = 'abcabcabc'
index = s.find('b')  # indexは1(2文字目)
print(index) # 1

## 第二引数で検索を開始する位置を指定できます。
s = 'abcabcabc'
index = s.find('b', 2)  # indexは4(5文字目)
print(index) # 4