import streamlit as st
import pandas as pd


def csv_viewer():
    st.title("CSVファイルアップローダー")

    # ファイルアップローダーを作成
    uploaded_file = st.file_uploader(
        "CSVファイルを選択してください", type=["csv"]
    )

    if uploaded_file is not None:
        try:
            # アップロードされたCSVファイルを読み込む
            df = pd.read_csv(uploaded_file)

            # データフレームの情報を表示
            st.write("## アップロードされたデータ")
            st.write(f"行数: {df.shape[0]}, 列数: {df.shape[1]}")

            # データフレームを表示
            st.write("## データフレーム")
            st.dataframe(df)

            # 列の統計情報を表示
            st.write("## 統計情報")
            st.write(df.describe())

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")


# if __name__ == '__main__':
#     csv_viewer()
csv_viewer()
