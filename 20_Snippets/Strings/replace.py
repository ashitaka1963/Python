str = 'abcdeabcde'
print(str)  # abcdeabcde
print(str.replace('cde','xyz'))  # abxyzabxyz


# 上記の方法だと'cde'が複数箇所にある場合に、すべて変換されてしまう。
# 特定の1箇所だけ変更したい場合には、以下の方法で変換を行う。

str = 'abcdeabcde'
r = 'xyz'
str = str[:2] + r + str[5:]
print(str) # abxyzabcde