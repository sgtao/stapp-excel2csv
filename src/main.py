import streamlit as st

"""
# Welcome to Streamlit!

Edit `/src` and `/tests` to customize this app to your heart's desire :heart:.
"""

# サイドバーのページに移動
# st.page_link("pages/example_app.py", label="Go to Example App")
st.page_link("pages/11_csv_viewer.py", label="Go to CSV Viewer App", icon="🚀")
st.page_link(
    "pages/12_excel_sheets.py", label="Go to Excel to CSV App", icon="🚀"
)
