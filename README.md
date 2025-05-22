# TODOList

## .bashrcに書いてほしいおまじない

このリポジトリでは、パーミッション関連の問題の回避のためにUID、GIDを使います。その設定のため、以下のコマンドを実行してください。

```bash
cat <<EOF >> ~/.bashrc
export USER_UID=$(id -u)
export USER_GID=$(id -g)
EOF
```

これで実行中のユーザーと同じパーミッションでファイルを生成、コンテナからコミットまでできます。
