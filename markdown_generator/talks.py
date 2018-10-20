#!/usr/bin/env python3

import pandas as pd
import re
import urllib.parse as ur
import os

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

talks = pd.read_json("talks.json")

for row, elm in talks.iterrows():
    item = elm.values[0]

    if len(str(item['date'])) > 5:
        ## make url_slug
        ## head 20
        title = re.sub(' +',' ',item['title'])
        url_slug = ur.quote(title[:20])

        md_filename = str(item['date']) + "-" + url_slug + ".md"
        html_filename = str(item['date']) + "-" + url_slug
        year = item['date'][:4]

        author = re.sub(' +',' ',item['author'])
        venue = re.sub(' +',' ',item['venue'])

        md = "---\ntitle: \""   + title + '"\n'
        md += "collection: talks" + "\n"

        if 'type' in item:
            md += 'type: "' + item['type'] + '"\n'
        else:
            md += 'type: "Talk"\n'

        md += "permalink: /talks/" + html_filename + "\n"

        if len(str(venue)) > 1:
            md += 'venue: "' + venue + '"\n'

        if 'date' in item:
            md += "date: " + str(item['date']) + "\n"

        if 'location' in item:
            md += 'location: "' + str(item['location']) + '"\n'

        if 'latitude' in item:
            md += 'latitude: "' + str(item['latitude']) + '"\n'
        if 'longitude' in item:
            md += 'longitude: "' +  str(item['longitude']) +'"\n'

        md += "---\n"



        if 'description' in item:
            md += "\n" + html_escape(item['description']) + "\n"


        #md_filename = os.path.basename(md_filename)
        print(md)

        #with open("../_talks/" + md_filename, 'w') as f:
        #    f.write(md)
