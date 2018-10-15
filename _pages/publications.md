---
layout: archive
title: "Publications (Refereed Papers)"
permalink: /publications/
author_profile: true
---

<!-- why author.googlescholr is empty? -->
You can also find my articles on <a href="https://scholar.google.co.jp/citations?user=aEJiKhAAAAAJ&hl=en">my Google Scholar profile</a>.


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
