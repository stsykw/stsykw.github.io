---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<!-- why is "author.googlescholr" empty? -->
You can also find my articles on <u><a href="https://scholar.google.co.jp/citations?user=aEJiKhAAAAAJ&hl=en">my Google Scholar profile</a></u>.



{% include base_path %}

{% if author.googlescholar %}
You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
