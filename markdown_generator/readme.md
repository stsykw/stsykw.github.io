# new data format

Edit `publications.json`, `talks.json` and `teaching.json` by an editor.
If you use the atom editor, you may want to install `atom-json-editor` plugin.
For generating each markdown file, use `publications.py`,  `talks.py` and `teaching.py`.


# Jupyter notebook markdown generator

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process. The .py files are pure python that do the same things if they are executed in a terminal, they just don't have pretty documentation.
