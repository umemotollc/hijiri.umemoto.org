# IIIF Static Archive

このページでは、冊子の画像IIIF形式で公開するための静的データ生成方法について説明します。

いわゆる static IIIF を提供するために、IIIF Presentation API 3.0に準拠したManifestをPythonで自動生成します。

## 1. ディレクトリ構成

```text
iiif-test
├── iiif-generate.py
├── index.html
├── manifests
│   └── MATSUMURA-Sotojiro-Passport-1931.json
├── requirements.txt
└── sotojiro-passport
    ├── passport-sotojiro-01.jpeg
    ├── passport-sotojiro-02.jpeg
    ├── passport-sotojiro-03.jpeg
    ├── passport-sotojiro-04.jpeg
    ├── passport-sotojiro-05.jpeg
    ├── passport-sotojiro-06.jpeg
    ├── passport-sotojiro-07.jpeg
    ├── passport-sotojiro-08.jpeg
    ├── passport-sotojiro-09.jpeg
    ├── passport-sotojiro-10.jpeg
    ├── passport-sotojiro-11.jpeg
    ├── passport-sotojiro-12.jpeg
    ├── passport-sotojiro-13.jpeg
    ├── passport-sotojiro-14.jpeg
    ├── passport-sotojiro-15.jpeg
    ├── passport-sotojiro-16.jpeg
    ├── passport-sotojiro-17.jpeg
    ├── passport-sotojiro-18.jpeg
    ├── passport-sotojiro-19.jpeg
    └── passport-sotojiro-20.jpeg
```

## 2. Python仮想環境の作成

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. ライブラリのインストール

```bash
python -m pip install --upgrade pip
pip install Pillow
```

```bash
pip freeze > requirements.txt
```

## 4. JPEG画像の配置

`sotojiro-passport/` には、パスポートのページ画像が置かれています。


## 5. Manifestの生成

以下を実行。

```bash
python iiif-generate.py
```

`manifests/` に次のファイルが生成される。

```text
manifests/
    MATSUMURA-Sotojiro-Passport-1931.json
```

Manifestには以下の情報が登録される。

- 資料名（日本語・英語）
- 資料種別
- 発行国
- 発行機関
- ページ画像
- ページ順序
- 画像サイズ

## 6. IIIF画像の配置

各JPEGについて、IIIF Image API 3.0 Level 0形式の画像データを生成し、以下のURLで公開。

```text
https://hijiri.umemoto.org/iiif-test/images/MATSUMURA-Sotojiro-Passport-1931/
```

各ページの `info.json` および画像ファイルは、Manifest内の参照URLと一致させる。

## 7. 公開

以下の構成をWebサーバーに配置する。

```text
iiif-test/
├── images/
│   └── MATSUMURA-Sotojiro-Passport-1931/
└── manifests/
    └── MATSUMURA-Sotojiro-Passport-1931.json
```

Manifestの公開URL：

```text
https://hijiri.umemoto.org/iiif-test/manifests/MATSUMURA-Sotojiro-Passport-1931.json
```

このURLをUniversal ViewerなどのIIIF対応ビューアーに指定することで、冊子を閲覧できる。

## 8. 仮想環境の終了

```bash
deactivate
```

---

**使用した道具**

- Python 3
- Pillow
- IIIF Image API 3.0
- IIIF Presentation API 3.0
- Universal Viewer