# test_pages_excel_sheets.py
import sys
import os
from streamlit.testing.v1 import AppTest

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

def test_show_title():
    """show title"""
    at = AppTest.from_file("src/pages/12_excel_sheets.py")
    at.run(timeout=30)  # タイムアウトを30秒に設定
    # print(f"at is {at}")
    assert at.title[0].value == "Excel to CSV App"
