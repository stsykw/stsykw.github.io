# Jupyter notebook markdown generator

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process. The .py files are pure python that do the same things if they are executed in a terminal, they just don't have pretty documentation.

# 今の構造

`presentations.tsv` `talks.tsv`は廃止。すべてexcelファイルに変更した。それにともない`presentations.py` `talks.py`もexcelファイルを扱うように変更。ファイル名などはExcelファイル上で自動生成している。
