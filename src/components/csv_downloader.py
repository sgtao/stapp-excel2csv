# csv_downloader.py
import streamlit as st
import pandas as pd


# CSVダウンロード用の関数
def download_csv(df: pd.DataFrame):
    """
    DataFrameをCSV形式に変換する関数
    Args:
        df (pd.DataFrame): 変換するDataFrame
    Returns:
        bytes: UTF-8 with BOMエンコーディングされたCSVデータ
    """
    csv = df.to_csv(index=False)
    # BOMを追加してExcelで文字化けしないようにして`return`する
    return csv.encode("utf-8-sig")


# CSVダウンロード用コンポーネント
def csv_downloader(df: pd.DataFrame, filename: str):
    """
    StreamlitアプリにCSVダウンロードボタンを追加するコンポーネント
    Args:
        df (pd.DataFrame): ダウンロードするDataFrame
        filename (str): ダウンロードされるCSVファイルの名前
    """
    try:
        csv = download_csv(df)

        if st.download_button(
            label="CSVファイルをダウンロード",
            data=csv,
            file_name=filename,
            mime="text/csv",
        ):
            # ダウンロードボタンがクリックされた場合
            st.success("ダウンロードが成功しました。")
    except Exception as e:
        # 例外が発生した場合
        st.error(f"エラー: ダウンロード中に問題が発生しました。 {str(e)}")
