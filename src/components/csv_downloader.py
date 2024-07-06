# csv_downloader.py
import streamlit as st
import pandas as pd


# CSVダウンロード用の関数
def download_csv(df: pd.DataFrame):
    csv = df.to_csv(index=False)
    # BOMを追加してExcelで文字化けしないようにして`return`する
    return csv.encode("utf-8-sig")


# CSVダウンロード用コンポーネント
def csv_downloader(df: pd.DataFrame, sheetname: str):
    csv = download_csv(df)
    filename = f"{sheetname}.csv"
    st.download_button(
        label="CSVファイルをダウンロード",
        data=csv,
        file_name=filename,
        mime="text/csv",
    )
