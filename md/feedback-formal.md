* {{ comment.paper }} {{ comment.year }}
  {% for c in comment.comments %}
  - {{ c }}
  {% endfor %}