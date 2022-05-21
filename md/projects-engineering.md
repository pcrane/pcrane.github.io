{% extends 'md/section.md' %}
{% block section_title %}Contract Developer{% endblock %}
{% block section_body %}
{% for project in projects %}
{% if project.type and project.type != "research" %}
{% include 'md/project.md' %}
{% endif %}
{% endfor %}
{% endblock %}