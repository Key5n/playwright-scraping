# Get Started

コンテナのビルドをする

```
docker build -t scraping .
```

コンテナで python ソースコードを実行する

```
docker run -it --rm scraping
```

# What's this

これは Microsoft が開発したブラウザ自動化ツールの **Playwright**を使用したプログラムです。
Playwright は主にフロントエンドの E2E テストやスクレイピングに使われます。
今回はタイトルや h1 要素のテキストの取得やスクリーンショットのみを実装しています。

# Playwright 開発環境構築の仕方

1. Playwright パッケージをインストールする
1. Playwright からブラウザをインストールする（Playwright はそのときのブラウザの最新版を使用するため）

- 以下のブラウザを選べる
  - Chromium
  - Firefox
  - Webkit
  - Google Chrome
  - Microsoft Edge
  - Mobile Chrome
  - Mobile Safari

1. Playwright の System-dependencies をインストールする
