# flask簡易ブログ

誰でも投稿ができる簡易的なブログサイトです。

ログイン不要で掲示板のように利用できます。
いいね、コメント機能があり承認欲求を満たすことができます。
## 仕様

- flaskを使った簡易的なブログサイト
- いいね機能
- コメント機能
- 編集、削除


## 使い方
 - Python
 - flask
 - peewee

が必要になります。

Pythonは 3.12.4 で開発、動作確認しています。

3.12.4 またはそれ以上のバージョンで実行してください。

## セットアップ

```
git clone https://github.com/2024AIT-OOP2-G18/flask-blog
```
```
pip install -r requirements.txt
```

実行する
```
python main.py
```

`http://localhost:8888` にアクセス


サンプルデータを使う場合は、以下のコマンドを実行してから実行してください。
```
cp database_sample.db database.db
```

