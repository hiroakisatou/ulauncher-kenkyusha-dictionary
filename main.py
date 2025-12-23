import json
import subprocess
import urllib.parse
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction


def get_clipboard_text():
    """クリップボードからテキストを取得"""
    try:
        # xclipを試す
        result = subprocess.run(['xclip', '-selection', 'primary', '-o'], 
                              capture_output=True, text=True, timeout=0.1)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except:
        pass
    
    try:
        # xselを試す
        result = subprocess.run(['xsel', '-p'], 
                              capture_output=True, text=True, timeout=0.1)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except:
        pass
    
    return None


class KenkyushaDictionaryExtension(Extension):

    def __init__(self):
        super(KenkyushaDictionaryExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument() or ""
        
        # クエリが空の場合はクリップボードから選択テキストを取得
        if not query.strip():
            clipboard_text = get_clipboard_text()
            if clipboard_text:
                search_term = clipboard_text.strip()
            else:
                return RenderResultListAction([
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name='検索語を入力してください',
                        description='研究社オンライン辞書で検索する単語を入力してください',
                        on_enter=ExtensionCustomAction(None)
                    )
                ])
        else:
            search_term = query.strip()
        
        # URLの構築（複数のcheckedBookパラメータを正しく処理）
        base_url = "https://kod.kenkyusha.co.jp/service/search/search_frame.jsp"
        query_string = "back=false&page=form.jsp&methodName=%95W%8F%80%8C%9F%8D%F5&sortkey=index&field={}&subMethod=wildcard&method=normal&book=normal-set&checkedBook=plus_e&checkedBook=eidai&checkedBook=eiwa&checkedBook=compass&checkedBook=wadai_j&checkedBook=waei&checkedBook=compass_waei&checkedBook=lumi_waei&checkedBook=plus_j".format(
            urllib.parse.quote(search_term)
        )
        
        url = f"{base_url}?{query_string}"
        
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name=f'研究社オンライン辞書で「{search_term}」を検索',
                description=url,
                on_enter=OpenUrlAction(url)
            )
        ])


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        if data:
            # カスタムアクションがあればここで処理
            pass


if __name__ == '__main__':
    KenkyushaDictionaryExtension().run()

