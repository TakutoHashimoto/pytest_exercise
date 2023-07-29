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

* 詳細な情報が必要な場合は、オプションで `-v` または `--verbose` を指定する。
```
=================================== test session starts ===================================
platform darwin -- Python 3.9.6, pytest-7.4.0, pluggy-1.2.0 -- /Users/takuto/.pyenv/versions/3.9.6/bin/python3
cachedir: .pytest_cache
rootdir: /Users/takuto/github/pytest_exercise/ch1
plugins: pep8-1.0.6
collected 1 item                                                                          

test_one.py::test_passing PASSED                                                    [100%]

==================================== 1 passed in 0.01s ====================================
```

### テストが失敗する場合
```
% pytest test_two.py 
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/takuto/github/pytest_exercise/ch1
plugins: pep8-1.0.6
collected 1 item                                                               

test_two.py F                                                            [100%]

=================================== FAILURES ===================================
_________________________________ test_failing _________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get more diff

test_two.py:2: AssertionError
=========================== short test summary info ============================
FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
============================== 1 failed in 0.02s ===============================
```
* テストが失敗した場合は、なぜ失敗したのかが `test_failing` という別のセクションに表示される。その失敗がインデックス0の不一致によるものであることがわかる。ターミナル上で実行している場合、赤色の文字で表示されるのでエラーの箇所が目立つ。この追加のセクションには、テストが失敗した正確な場所とその周囲のコードが表示される。このセクションを **トレースバック(traceback)** という。