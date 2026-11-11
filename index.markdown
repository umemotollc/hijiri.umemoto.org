---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
author: Hijiri UMEMOTO
layout: home
title: Hijiri UMEMOTO
---

## スライド Slides

- [『ウィキピディア』と『ウィキペディア』](./slides/2026-03-01-wikimedia25.html)
- [電気通信大学メモ(1)（2026-11-05）](./slides/2026-11-05-dentsudai.html)
- [Markdownでスライドを作る方法](README.slides.md)

## 実験室

### Omeka S + Hugo

- [砺波市美術館で見つけた謎の家族写真 - Omeka S + Hugo を使った静的HTMLの例](./omeka-s/)
- [Omeka S + Hugo の使い方](README.omeka.md)

[_Omeka S_](https://omeka.org/s/) という文化資源を扱うソフトウエアから出力した静的データを _Hugo_ を使ってHTMLに変換しています。内容については単なる見本で、権利処理で問題がなさそうな家族写真を載せています。Omeka S は、ノートパソコンに入れて持ち歩いています。

### 静的データで IIIF を実現しよう

いわゆる静的IIIF (IIIF Level 0, static IIIF image server) の手法でマニフェストを公開し、静的なウェブサーバ (github pages) で画像をホストする方法をテストしています。pythonスクリプトでマニフェストのjson出力と画像変換を行いました。表示には、universal viewer を使っています。サンプルの画像は、私の先祖のパスポート(1931年発行、砺波市美術館所蔵)です。 

- [松村外次郎 パスポート, 1931 - IIIF画像をスタティックに表示する例](./iiif-test/)
- [README.md](./iiif-test/README.md)