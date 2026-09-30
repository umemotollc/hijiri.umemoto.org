# Omeka S (Hugo) から GitHub Pages への静的サイト公開マニュアル

Omeka Sの「Static Site Export」モジュールから出力されたHugo用ソースコードをビルドし、GitHub PagesでWebサイトとして公開するまでの手順です。

---

## 前提条件
- お手元のMacに **Homebrew** がインストールされていること。
- **GitHubアカウント** を持っていること。

---

## Step 1: MacにHugoをインストールする

Omeka Sから出力されたデータ（`hugo.json` や `content` フォルダなど）は、静的サイトジェネレーター「Hugo」の原材料です。これをHTMLに変換するため、MacにHugoをインストールします。

1. ターミナルを開きます。
2. 以下のコマンドを実行してHugoをインストールします。
   ```bash
   brew install hugo
   ```
3. インストールが成功したか確認します。
   ```bash
   hugo version
   ```

---

## Step 2: サイト設定（baseURL）の修正

GitHub Pagesでデザイン（CSSや画像）が崩れないようにするため、設定ファイルを書き換えます。

1. フォルダの直下にある **`hugo.json`** をテキストエディタ（VS Codeやテキストエディットなど）で開きます。
2. `baseURL` の項目を、将来公開されるGitHub PagesのURLに変更して保存します。
   ```json
   "baseURL": "https://[あなたのGitHubユーザー名].github.io/[作成するリポジトリ名]/"
   ```
   *(※ 最後のスラッシュ `/` を忘れないようにしてください)*

---

## Step 3: 静的HTMLの生成（ビルド）

1. ターミナルで `hugo.json` があるフォルダ（例: `sotojiro-shiryo-1790785443`）に移動します。
   ```bash
   cd /path/to/sotojiro-shiryo-1790785443
   ```
2. 以下のコマンドを実行してビルドします。
   ```bash
   hugo
   ```
3. 成功すると、フォルダ内に新しく **`public`** というフォルダが自動生成されます。この中に `index.html` を含む公開用の全ファイルが書き出されます。

---

## Step 4: GitHubでリポジトリを作成する

1. [GitHub](https://github.com) にログインし、右上の「**+**」アイコン ➔ 「**New repository**」をクリックします。
2. 以下の通り設定します。
   - **Repository name**: `hugo.json` で指定したリポジトリ名と同じもの
   - **Public / Private**: 必ず **Public** を選択（無料プランでPagesを使うため）
   - その他：初期化チェックボックスはすべて外したままでOK
3. 「**Create repository**」をクリックします。

---

## Step 5: ファイルのアップロード

1. リポジトリ作成直後の画面にある「**uploading an existing file**」という青いリンクをクリックします。
2. MacのFinderで、Step 3で生成された **`public` フォルダを開きます。**
3. **`public` フォルダの中身（`index.html`、`assets`、`items` などのフォルダ群）をすべて選択し、ブラウザの画面にドラッグ＆ドロップします。**
   - ⚠️ *注意: `public` フォルダ自体をドロップするのではなく、必ず「中身」を全選択して入れてください。*
4. 画面下部の「**Commit changes**」ボタンをクリックして保存します。

---

## Step 6: GitHub Pagesの有効化

1. リポジトリ画面上部の「⚙️ **Settings**（設定）」タブをクリックします。
2. 左メニューから「Code and automation」➔「**Pages**」をクリックします。
3. 「Build and deployment」の **Branch** 設定を、`None` から **`main`**（または `master`）に変更します。
4. フォルダは **`/root`** のまま、右側の「**Save**」をクリックします。

---

## Step 7: 公開確認

1. 設定保存後、1〜2分待ってから「Pages」画面をリロードします。
2. 画面上部に **「Your site is live at [URL]」** と表示されたら公開完了です。
3. リンクをクリックし、サイトが正常に表示されるか（画像やデザインが崩れていないか）確認してください。
