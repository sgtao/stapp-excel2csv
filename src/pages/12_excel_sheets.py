import os
import streamlit as st
import pandas as pd
import openpyxl

from components.csv_downloader import csv_downloader


def excel_sheets():
    st.title("Excel to CSV App")

    # ファイルアップローダーを作成
    uploaded_file = st.file_uploader(
        "Excelファイルを選択してください", type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            # print(uploaded_file.name)
            excel_filename = uploaded_file.name
            # 拡張子を除去したファイル名を取得
            filename_without_extension = os.path.splitext(excel_filename)[0]

            # Excelファイルを読み込む
            wb = openpyxl.load_workbook(uploaded_file)

            # シート名のリストを取得
            sheet_names = wb.sheetnames

            # シート名を表示
            # st.write("## アップロードされたExcelファイルのシート一覧")
            st.subheader(f"ファイル：{excel_filename} のシート一覧")
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
                with st.expander("Download to CSV file?"):
                    download_filename = (
                        filename_without_extension
                        + "_"
                        + selected_sheet
                        + ".csv"
                    )
                    st.write(f"Filename is {download_filename}")
                    csv_downloader(df, download_filename)

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")


# if __name__ == '__main__':
#     excel_sheets()
excel_sheets()
