#!/usr/bin/env python3
# coding: utf-8

# # Publications markdown generator for academicpages
#
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
#
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
#

# ## Data format
#
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top.
#
# - `excerpt` and `paper_url` can be blank, but the others must have values.
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
#
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
#
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
#
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

#publications = pd.read_csv("publications.tsv", sep="\t", header=0)
publications = pd.read_excel("publications.xlsx",  header=0)

import os,math
id=1
for row, item in publications.iterrows():
    if len(str(item.pub_date)) > 5:

        md = "{\n  \"id\": \""   + str(id) + "\",\n"
        id += 1
        md += "  \"pub_date\": \""   + item.pub_date + "\",\n"
        if item.refereed == 1:
            md += "  \"refereed\": true,\n"
        else:
            md += "  \"refereed\": false,\n"
        md += "  \"title\": \"" + item.title +"\",\n"
        md += "  \"author\": \"" + item.author +"\",\n"
        md += "  \"venue\": \"" + item.venue +"\",\n"
        if not math.isnan(item.volume):
            md += "  \"volume\": \""  + str(int(item.volume)) +"\",\n"
        md += "  \"start\": \"" + str(item.start) +"\",\n"
        if not math.isnan(item.end):
            md += "  \"end\": \"" + str(int(item.end)) +"\",\n"
        #else:
        #    md += "  \"end\": ,\n"
        md += "  \"year\":\""  + str(int(item.year)) +"\",\n"
        md += "  \"doi\": \"" + str(item.doi) +"\"\n},"

        print(md)
#print(publications.to_json(orient='table'))
#print(pd.io.json.build_table_schema(publications))publications
