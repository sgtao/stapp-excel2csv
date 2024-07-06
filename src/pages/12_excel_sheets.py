import streamlit as st
import pandas as pd
import openpyxl

from components.csv_downloader import csv_downloader


def excel_sheets():
    st.title("Excelファイルアップローダー")

    # ファイルアップローダーを作成
    uploaded_file = st.file_uploader(
        "Excelファイルを選択してください", type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            # Excelファイルを読み込む
            wb = openpyxl.load_workbook(uploaded_file)

            # シート名のリストを取得
            sheet_names = wb.sheetnames

            # シート名を表示
            st.write("## アップロードされたExcelファイルのシート一覧")
            for i, sheet_name in enumerate(sheet_names, 1):
                st.write(f"{i}. {sheet_name}")

            # シートを選択するオプションを追加
            selected_sheet = st.selectbox(
                "表示するシートを選択してください", sheet_names
            )

            if selected_sheet:
                # 選択されたシートのデータを読み込む
                df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)

                # データフレームを表示
                st.write(f"## {selected_sheet}のデータ")
                st.dataframe(df)

                # ダウンロードボタンの作成
                if st.button("CSVダウンロード"):
                    csv_downloader(df, selected_sheet)

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")


# if __name__ == '__main__':
#     excel_sheets()
excel_sheets()
