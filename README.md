# mypkg
このパッケージは2024年ロボットシステム学課題２で作成したROS2のパッケージです。

# keyboard-talkerノード
[![test](https://github.com/aidadaichi49/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/aidadaichi49/mypkg/actions/workflows/test.yml)

## テスト環境
- ubuntu22.04

## 概要

- このノードはユーザからのキーボード入力をパブリッシュします。

- 直接的に口では伝えられない状況でも、このノードを使うことで簡単に伝えることができます。

- 手元でパブリッシュできているか分かるようになっています。

## 使用方法

- はじめに当リポジトリをクローンしてください。
```
$ git clone https://github.com/aidadaichi49/mypkg.git
```

- 実行する際は以下の形式で実行してください。
```
$ ros2 run mypkg keyboard_talker
hello
[INFO] [1736010124.617157728] [keyboard_talker]: Published message: hello
```

- パブリシティされているか確認するときには違う端末を使って以下のように確認できます。
```
$ ros2 topic echo /keyboard_input
data: hello
```

- 終了するにはexitを入力して終了してください。
```
[INFO] [1736010124.617157728] [keyboard_talker]: Published message: hello
exit
```

## ライセンス
- このパッケージは, 3条項BSDライセンスの下, 再配布および使用が許可されます.
- @2025 Daichi Aida
