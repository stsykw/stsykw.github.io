---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<!-- why is "author.googlescholr" empty? -->
You can also find my articles on <u><a href="https://scholar.google.co.jp/citations?user=aEJiKhAAAAAJ&hl=en">my Google Scholar profile</a></u>.

{% include base_path %}

## Refereed Papers
(Jump to <a href="#other">other papers</a>)

{% for post in site.publications reversed %}
  {% if post.refereed == 'True' %}
    {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

## <a name="other">Other Papers</a>

{% for post in site.publications reversed %}
  {% if post.refereed != 'True' %}
    {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}
