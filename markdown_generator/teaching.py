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

teaching = pd.read_json("teaching.json")

for row, elm in teaching.iterrows():
    item = elm.values[0]

    if len(str(item['year'])) > 3:
        ## make url_slug
        ## head 20
        title = re.sub(' +',' ',item['title'])
        year = str(item['year'])
        url_slug = str(item['url_slug'])

        md_filename = year + "-" + str(item['semester']) + "-" + url_slug + ".md"
        html_filename = year + "-" + str(item['semester']) + "-" + url_slug

        venue = re.sub(' +',' ',item['venue'])

        md = "---\ntitle: \""   + title + '"\n'
        md += "collection: teaching" + "\n"

        if 'type' in item:
            md += 'type: "' + item['type'] + '"\n'

        md += "permalink: /teaching/" + html_filename + "\n"

        if len(str(venue)) > 1:
            md += 'venue: "' + venue + '"\n'

        if item['semester'] == "spring":
            md += "date: " + year + "-04-01\n"
        elif item['semester'] == "autumn":
            md += "date: " + year + "-10-01\n"
        elif item['semester'] == "summer":
            md += "date: " + year + "-06-01\n"
        elif item['semester'] == "winter":
            md += "date: " + year + "-12-01\n"

        course_url = "/courses/" + html_filename
        md += 'course_url: '+ course_url + '\n'

        if 'location' in item:
            md += 'location: "' + str(item['location']) + '"\n'

        md += "---\n"

        md += "\n" + venue + "\n"
        if 'description' in item:
            md += "\n" + html_escape(item['description']) + "\n"

        ## これは良くない
        md += "\n\n<a href='https://stsykw.github.io" + course_url + "'>Course Page</a>\n"

        md_filename = os.path.basename(md_filename)

        #print(md)

        with open("../_teaching/" + md_filename, 'w') as f:
            f.write(md)
