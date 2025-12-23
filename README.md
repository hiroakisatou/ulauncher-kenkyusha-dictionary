# 研究社オンライン辞書検索 - Ulauncher Extension

選択したテキストまたは入力したテキストで研究社オンライン辞書を検索するUlauncher拡張機能です。

## 機能

- 選択したテキストまたは入力したテキストで研究社オンライン辞書を検索
- ブラウザで検索結果を開く
- クリップボードから選択テキストを自動取得

## インストール

### Ulauncherからインストール

1. Ulauncherを開く（デフォルト: `Ctrl+Space`）
2. 設定（Preferences）を開く
3. Extensions タブを選択
4. "Add extension" をクリック
5. このリポジトリのURLを入力:
   ```
   https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary
   ```
6. "Add" をクリック

### 手動インストール

```bash
cd ~/.config/ulauncher/extensions
git clone https://github.com/YOUR_USERNAME/ulauncher-kenkyusha-dictionary.git kenkyusha-dictionary
```

その後、Ulauncherを再起動してください。

## 使用方法

1. Ulauncherを開く（デフォルト: `Ctrl+Space`）
2. `kod` と入力（デフォルトキーワード）
3. 検索したい単語を入力（または事前にテキストを選択）
4. Enterキーで検索結果をブラウザで開く

## カスタマイズ

### キーワードの変更

1. Ulauncherの設定を開く
2. Extensions タブを選択
3. "研究社オンライン辞書検索" を選択
4. Preferences でキーワードを変更

または、`manifest.json` の `default_value` を編集してください。

## 要件

- Ulauncher
- Python 3.x
- xclip または xsel（選択テキストの取得に使用）

## ライセンス

MIT License

## 作者

Your Name

## 問題報告

問題や改善提案がある場合は、GitHubのIssuesで報告してください。

