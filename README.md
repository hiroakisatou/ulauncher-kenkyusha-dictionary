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
   https://github.com/hiroakisatou/ulauncher-kenkyusha-dictionary
   ```
6. "Add" をクリック

### 手動インストール

```bash
cd ~/.config/ulauncher/extensions
git clone https://github.com/hiroakisatou/ulauncher-kenkyusha-dictionary.git kenkyusha-dictionary
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

### 依存関係のインストール

xclipがインストールされていない場合は、以下のコマンドでインストールしてください：

**Ubuntu/Debian:**
```bash
sudo apt install xclip
```

**Fedora:**
```bash
sudo dnf install xclip
```

**Arch Linux:**
```bash
sudo pacman -S xclip
```

**または xsel を使用する場合:**
```bash
sudo apt install xsel  # Ubuntu/Debian
sudo dnf install xsel  # Fedora
sudo pacman -S xsel    # Arch Linux
```

## ライセンス

MIT License

## 作者

tsu-na-gu

## トラブルシューティング

### 選択テキストが取得できない

選択したテキストが自動的に検索されない場合は、xclip または xsel がインストールされているか確認してください：

```bash
which xclip
# または
which xsel
```

いずれもインストールされていない場合は、上記の「依存関係のインストール」セクションを参照してください。

### 拡張機能が表示されない

Ulauncherを再起動してください：

```bash
ulauncher-toggle  # Ulauncherを再起動
# または
killall ulauncher && ulauncher &
```

## 問題報告

問題や改善提案がある場合は、GitHubのIssuesで報告してください：
https://github.com/hiroakisatou/ulauncher-kenkyusha-dictionary/issues

