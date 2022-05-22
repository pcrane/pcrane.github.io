{% extends 'md/section.md' %}

{% block section_title %}Awards and Honours{% endblock %}

{% block section_body %}
{% for award in awards %}
{% include 'md/award.md' %}
{% endfor %}
{% endblock %}