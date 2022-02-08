# python-lib-for-me <!-- omit in toc -->


# 0. 目次 <!-- omit in toc -->

- [1. 概要](#1-概要)
- [2. 機能](#2-機能)
- [3. 動作確認済み環境](#3-動作確認済み環境)
- [4. セットアップ手順](#4-セットアップ手順)
- [5. 使い方](#5-使い方)
- [6. 連絡先](#6-連絡先)
- [7. ライセンス](#7-ライセンス)


# 1. 概要

自分用のPythonライブラリ。

PyPIには登録せずにローカルで使用する。


# 2. 機能

下記モジュールをアプリケーションから利用できる。

- 日付モジュール
  - 今月初日取得関数
  - 今月末日取得関数
  - 来月初日取得関数
  - 来月末日取得関数
  - 先月初日取得関数
  - 先月末日取得関数
- 例外モジュール
  - 自作例外クラス
- ロガーモジュール
  - ロガー取得関数


# 3. 動作確認済み環境

- Windows 10 Pro
- Python 3.10.1
- Pipenv 2022.1.8


# 4. セットアップ手順

まず、セットアップにあたり前提として、PythonとPipenvがインストール済みであること。

本リポジトリをクローンもしくはダウンロードした後、下記コマンドを実行する。

```cmd
> cd [application_path]             # ライブラリをインストールしたいアプリケーションのパスに移動する
> pipenv install -e [library_path]  # ライブラリのパスを指定して編集モードでインストールする
```

実行例：
```cmd
> cd fgo-farm-report-collection
> pipenv install -e "../python-lib-for-me"

Installing -e ../python-lib-for-me...
Adding python-lib-for-me to Pipfile's [packages]...
Installation Succeeded
Pipfile.lock (e4eef2) out of date, updating to (2271fc)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
           Building requirements...
Resolving dependencies...
Success!
Updated Pipfile.lock (2271fc)!
Installing dependencies from Pipfile.lock (2271fc)...
  ================================ 0/0 - 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```


# 5. 使い方

下記コードでアプリケーションから機能を呼び出す。

実装例：
```python
import python_lib_for_me
python_lib_for_me.do_function()
```


# 6. 連絡先

[Twitter(@silverag_corgi)](https://twitter.com/silverag_corgi)


# 7. ライセンス

MITライセンスの下で公開している。
詳細はLICENSEを確認すること。

