# GitHubリポジトリのセットアップ手順

## 1. GitHubリポジトリの作成

1. GitHubにログイン
2. 右上の「+」をクリック > "New repository"
3. リポジトリ名を入力: `ulauncher-kenkyusha-dictionary`
4. Description: "研究社オンライン辞書検索 - Ulauncher Extension"
5. Public を選択
6. "Create repository" をクリック

## 2. リポジトリのURLを更新

`manifest.json` と `README.md` の以下の部分を実際のGitHubユーザー名に置き換えてください:

- `YOUR_USERNAME` → あなたのGitHubユーザー名

## 3. ファイルをGitHubにプッシュ

```bash
cd /home/tsu-na-gu/Development/elixir_in_action/ulauncher

# Gitリポジトリを初期化
git init

# ファイルを追加
git add .

# コミット
git commit -m "Initial commit: 研究社オンライン辞書検索プラグイン"

# リモートリポジトリを追加（YOUR_USERNAMEを実際のユーザー名に置き換え）
git remote add origin https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary.git

# プッシュ
git branch -M main
git push -u origin main
```

## 4. Ulauncherからインストール

1. Ulauncherを開く
2. 設定（Preferences）を開く
3. Extensions タブを選択
4. "Add extension" をクリック
5. リポジトリのURLを入力:
   ```
   https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary
   ```
6. "Add" をクリック

## 注意事項

- アイコンファイル（`images/icon.png`）が存在しない場合、Ulauncherがデフォルトアイコンを使用します
- 必要に応じて、`images/icon.png` を64x64ピクセルのPNG画像に置き換えてください

