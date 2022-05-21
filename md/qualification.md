{%- macro meta(qualification) -%}
{{qualification.subject}}, {{qualification.where.text}}, {{qualification.when.end.year}}
{% endmacro -%}
{%- macro abstract(qualification) -%}
{% if qualification.abstract.visible -%}
_{{ link_format(qualification.title.href, qualification.title.text, qualification.title.onclick) }}_
{{qualification.abstract.short}}
{%- endif -%}
{%- endmacro %}
### {{qualification.what}} 
{{ meta(qualification) }}
{{ abstract(qualification) }}
