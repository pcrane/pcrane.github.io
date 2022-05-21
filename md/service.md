{% extends 'md/section.md' %}

{% block section_title %}Service{% endblock %}
{% block section_body %}
{% with s=service %}
{% for service in s %}
{% include 'md/service.md' %}
{% endfor %}
{% endwith %}
{% endblock %}
