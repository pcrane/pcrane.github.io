{% extends 'md/section.md' %}

{% block section_title %}Education{% endblock %}

{% block section_body %}
{%- for qualification in education if qualification.visible -%}
{% include 'md/qualification.md' %}
{% endfor -%}
{%- endblock -%}