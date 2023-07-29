# Chapter1
## pytestのインストール
```
pip install pytest
```

## pytestの実行
* ターミナル上で以下のように入力することでテストが実行される。

```
% cd <ch1のパス>
% pytest test_one.py
```
テストを実行すると以下のような結果が表示される（今回は成功している）。
```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/takuto/github/pytest_exercise/ch1
plugins: pep8-1.0.6
collected 1 item                                                               

test_one.py .                                                            [100%]

============================== 1 passed in 0.01s ===============================
```