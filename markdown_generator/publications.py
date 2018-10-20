#!/usr/bin/env python3

import pandas as pd
import re
import urllib.parse as ur

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

publications = pd.read_json("publications.json")

for row, elm in publications.iterrows():
    item = elm.values[0]

    if len(str(item['pub_date'])) > 5:
        ## make url_slug
        ## head 20
        title = re.sub(' +',' ',item['title'])
        url_slug = ur.quote(title[:20])

        md_filename = str(item['pub_date']) + "-" + url_slug + ".md"
        html_filename = str(item['pub_date']) + "-" + url_slug
        year = item['pub_date'][:4]

        author = re.sub(' +',' ',item['author'])
        venue = re.sub(' +',' ',item['venue'])
        ## YAML variables

        md = "---\ntitle: \""   + title + '"\n'

        md += """collection: publications"""

        md += """\npermalink: /publication/""" + html_filename

        if 'excerpt' in item:
            md += "\nexcerpt: '" + html_escape(item['excerpt']) + "'"

        md += "\ndate: " + str(item['pub_date'])

        md += "\nvenue: '" + html_escape(venue) + "'"

        ## make paper_url fron item['doi']
        paper_url = ''
        if 'doi' in item:
            paper_url += "https://dx.doi.org/" + item['doi']
            md += "\npaperurl: '" + paper_url + "'"

        ## make citations
        citation ="{}, {}, {}".format(author,title,venue)
        if 'volume' in item:
            citation += ", <b>{}</b>".format(item['volume'])
        if 'start' in item:
            citation += ", {}".format(item['start'])
        if 'end' in item:
            citation += "-{}".format(item['end'])
        if 'year' in item:
            citation += ", ({})".format(item['year'])
        md += "\ncitation: '" + html_escape(citation) + "'"

        md += "\n---"

        ## Markdown description for individual page


        md += "\n\nAuthor(s): " + author + "\n"

        if 'comments' in item:
            md += "\n\nComments: " + item['comments'] + "\n"

        if len(str(paper_url)) > 5:
            md += "\n\n<a href='" + paper_url + "'>Download paper here</a>\n"

        if 'excerpt' in item:
            md += "\n" + html_escape(item['excerpt']) + "\n"


        print(md)
