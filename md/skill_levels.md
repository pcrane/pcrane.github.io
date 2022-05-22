{%  extends 'md/section.md' %}

{% macro to_table_row(item) %}
| {{item.name}} | {% for detail in item.details %} {{detail.name}} {% endfor %}|
{%- endmacro %}

{% block section_title %}Technical Knowledge{% endblock %}
{% block section_body %}
|                  |                             |
|------------------|-----------------------------|
{%- for item in skill_levels.languages -%}
{{ to_table_row(item) }}
{%- endfor -%}
{%- for item in skill_levels.tools -%}
{{ to_table_row(item) }}
{%- endfor %}
{% endblock %}