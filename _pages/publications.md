---
layout: archive
title: "Publications (Refereed Papers)"
permalink: /publications/
author_profile: true
---

<!-- why author.googlescholr is empty? -->
You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
