#!/bin/bash
# GitHubリポジトリのセットアップスクリプト

echo "GitHubリポジトリのセットアップを開始します..."
echo ""

# Gitリポジトリを初期化
if [ ! -d .git ]; then
    git init
    echo "✓ Gitリポジトリを初期化しました"
else
    echo "⚠ Gitリポジトリは既に初期化されています"
fi

# ファイルを追加
git add .

# コミット
git commit -m "Initial commit: 研究社オンライン辞書検索プラグイン" 2>/dev/null || echo "⚠ コミットに失敗しました（既にコミット済みの可能性があります）"

echo ""
echo "次のステップ:"
echo "1. GitHubでリポジトリを作成: https://github.com/new"
echo "2. リポジトリ名: ulauncher-kenkyusha-dictionary"
echo "3. 以下のコマンドを実行（YOUR_USERNAMEを実際のユーザー名に置き換え）:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. manifest.json と README.md の YOUR_USERNAME を実際のユーザー名に置き換えてください"
