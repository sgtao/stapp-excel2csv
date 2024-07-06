# stapp-excel2csv
[streamlit](https://streamlit.io/)で、Webページ上でCSVをExcelに変換する機能を提供する

## Usage
- [poetry cli](https://cocoatomo.github.io/poetry-ja/cli/)を利用する

### Setup
```sh
poetry install
poetry shell
```

### コマンド一覧
```sh
$ task --list
start      streamlit run src/main.py
test       pytest tests
test-cov   pytest tests --cov --cov-branch -svx
test-repo  pytest tests --cov --cov-report=html
format     black --line-length 79 src
lint       flake8 src
check-format black整形とflake8チェックを実行
```

### Start as local service
```sh
# on poetry shell
# streamlit hello
# streamlit run src/main.py
task start
# Local URL: http://localhost:8501
```


### format and lint check
```sh
# task format
# task lint
task check-format
```


### Test with `pytest`
- [streamlitのテスト手法](https://docs.streamlit.io/develop/concepts/app-testing/get-started)を参考にテストを実施
```sh
# on poetry shell
# pytest tests/test_main.py
task test
```

### Test coverage

#### show c1 coverage
```sh
# on poetry shell
task test-cov
```

#### output HTML coverage report
```sh
# on poetry shell
task test-repo
```


## 他プロジェクトでの利用手順
### 01. リポジトリURLの変更
- `git-clone`したあと、`git-remote`でoriginを変更する
```sh
git clone https://github.com/sgtao/stpyapp-template.git stapp-excel2csv
cd stapp-excel2csv
# git remote add origin https://github.com/sgtao/stapp-excel2csv.git
git remote set-url origin https://github.com/sgtao/stapp-excel2csv.git
git branch -M main
git push -u origin main
```

### 02．`README.md`・`LICENSE`ファイルの変更
- `README.md`の変更：
  - タイトル、概要を変更する
  - LICENSEを変更する場合は、`README.md`の下段の表記と`LICENSE`ファイルを変更する

### 03．`src/pages`フォルダ配下にアプリケーション追加
- 例）`src/pages/11_csv_viewer.py`を作成
  - `task start`・`task check-format`などで確認
```py
import streamlit as st
import pandas as pd


def csv_viewer():
    st.title("CSVファイルアップローダー")

    ...

# if __name__ == '__main__':
#     csv_viewer()
csv_viewer()
```

## License
Apache-2.0 license
