# AtCorder用フォルダ作成スクリプト

カレントディレクトリ内にAtCorer用のフォルダおよびpyファイルを作成する。
現時点では、AtCoder Beginner Contestのフォルダのみ作成している。
コンテスト数が増えた場合は、「contest_nums = 160」の値を変更する。

フォルダ階層は以下になる。

AtCorder/
　└ ABC/
　 　├ ABC001/
　 　│　　├ ABC001_A.py
　 　│　　├ ABC001_B.py
　 　│　　├ ABC001_C.py
　 　│　　└ ABC001_D.py
　 　├ ABC002/
　 　│　　├ ABC002_A.py
　 　│　　├ ABC002_B.py
　 　│　　├ ABC002_C.py
　 　│　　└ ABC002_D.py
　 　・・・
　 　├ ABC126/
　 　│　　├ ABC126_A.py
　 　│　　├ ABC126_B.py
　 　│　　├ ABC126_C.py
　 　│　　└ ABC126_D.py
　 　│　　├ ABC126_E.py
　 　│　　└ ABC126_F.py
　 　・・・
　 　└ ABC160/
　 　 　　├ ABC160_A.py
　 　 　　├ ABC160_B.py
　 　 　　├ ABC160_C.py
　 　 　　└ ABC160_D.py
　 　 　　├ ABC160_E.py
　 　 　　└ ABC160_F.py
