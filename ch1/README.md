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

## pytestの実行方法
* `pytest <ファイル名>` でテストを実行することがわかった。
* ファイルやディレクトリを指定しない場合は、カレントディレクトリ以下で `pytest` がテストを検索する。
* `pytest` が検索するのは、ファイル名が `test_` で始まる、もしくは `_test` で終わる `.py` ファイル。

```
% pytest --tb=no
=================================== test session starts ===================================
platform darwin -- Python 3.9.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/takuto/github/pytest_exercise/ch1
plugins: pep8-1.0.6
collected 2 items                                                                         

test_one.py .                                                                       [ 50%]
test_two.py F                                                                       [100%]

================================= short test summary info =================================
FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
=============================== 1 failed, 1 passed in 0.02s ===============================
```

* ここでは、詳細な出力は必要ないので `--tb=no` を使ってトレースバックをオフにしている。

### テストディスカバリ
* `pytest` の実行のうち、実行するテストを検索する部分を **テストディスカバリ(test discovery)** という。これまでの例で `pytest` がすべて検出できたのは、それらのテストに `pytest` の命名規則に準拠した名前が付けられていたため。
* `pytest` がテストコードを検出できるようにするための命名規則
    * テストファイル: `test_<something>.py` もしくは `<something>_test.py`
    * テストメソッド: `test_<something>`
    * テストクラス: `Test<Something>`
* 基本的には上記のルールに従うが、これに従わない名前がついたテストがたくさんある場合は、テストディスカバリのルールを変更するやり方もある。