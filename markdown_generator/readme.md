# new structure

Edit `publications.json` and `talks.json` by atom editor or something.
In the atom, you must install `atom-json-editor` plugin.
For generating each markdown files, use `publications.py` and `talks.py`.

## 古い情報
`presentations.tsv` `talks.tsv`は廃止。すべてExcelファイルに変更した。それにともない`presentations.py` `talks.py`もExcelファイルを扱うように変更。markdownファイル名などはExcelファイル上で自動生成している。


# Jupyter notebook markdown generator

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process. The .py files are pure python that do the same things if they are executed in a terminal, they just don't have pretty documentation.
