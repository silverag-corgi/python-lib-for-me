# python-lib-for-me <!-- omit in toc -->


# 0. 目次 <!-- omit in toc -->

- [1. 概要](#1-概要)
- [2. 機能](#2-機能)
- [3. 動作確認済み環境](#3-動作確認済み環境)
- [4. セットアップ手順](#4-セットアップ手順)
  - [4.1. リポジトリのクローン](#41-リポジトリのクローン)
  - [4.2. 依存関係の追加](#42-依存関係の追加)
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
- 処理時間モジュール
  - 処理時間計測デコレータ関数


# 3. 動作確認済み環境

- Windows 10 Pro
- Python 3.10.1
- Poetry 1.1.12


# 4. セットアップ手順

まず、前提として、PythonとPoetryがインストール済みであること。


## 4.1. リポジトリのクローン

下記リポジトリをクローンもしくはダウンロードする。

- python-lib-for-me
  - 本リポジトリ


## 4.2. 依存関係の追加

下記コマンドを実行する。

```cmd
> cd [app_path]                             # ライブラリをインストールしたいアプリケーションのパスに移動する
> poetry add "../python-lib-for-me"         # 仮想環境にライブラリを追加する
```

もし、ライブラリを編集可能モードで追加する場合は、`pyproject.toml`ファイルに`develop = true`を追記する。

```toml
[tool.poetry.dependencies]
python-lib-for-me = {path = "../python-lib-for-me", develop = true}
```

下記コマンドを実行する。

```cmd
> poetry update                             # pyproject.tomlを基に仮想環境をアップデートする
```


# 5. 使い方

下記コードでアプリケーションから機能を呼び出す。

```python
import python_lib_for_me
python_lib_for_me.do_function()
```


# 6. 連絡先

[Twitter(@silverag_corgi)](https://twitter.com/silverag_corgi)


# 7. ライセンス

MITライセンスの下で公開している。
詳細はLICENSEを確認すること。

