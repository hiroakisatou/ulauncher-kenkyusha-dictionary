# クイックスタート

## GitHubにプッシュする手順

1. GitHubでリポジトリを作成:
   - https://github.com/new
   - リポジトリ名: `ulauncher-kenkyusha-dictionary`
   - Public を選択

2. 以下のコマンドを実行（YOUR_USERNAMEを実際のユーザー名に置き換え）:

```bash
cd /home/tsu-na-gu/Development/elixir_in_action/ulauncher

# Gitリポジトリを初期化
git init

# ファイルを追加
git add .

# コミット
git commit -m "Initial commit: 研究社オンライン辞書検索プラグイン"

# リモートリポジトリを追加
git remote add origin https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary.git

# プッシュ
git branch -M main
git push -u origin main
```

3. manifest.json と README.md の `YOUR_USERNAME` を実際のユーザー名に置き換える

4. Ulauncherからインストール:
   - Ulauncher設定 > Extensions > Add extension
   - URL: `https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary`
