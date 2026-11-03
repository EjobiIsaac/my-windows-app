import webview
import os
import sys

def get_index_path():
    # When built as EXE, file is inside temp folder
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'index.html')

if __name__ == '__main__':
    url = get_index_path()
    # Create ABRA window - Big Enterprise size
    window = webview.create_window(
        'ABRA FINANCES 🇺🇬 - BIG ENTERPRISE v2.0',
        url,
        width=1200,
        height=800,
        min_size=(900, 600),
        resizable=True
    )
    webview.start()
