{%- macro meta(qualification) -%}
{{qualification.subject}}, {{link_format(qualification.where)}}, {{qualification.when.end.year}}
{% endmacro -%}
{%- macro abstract(qualification) -%}
{% if qualification.abstract.visible -%}
_{{ link_format(qualification.title) }}_
{{qualification.abstract.short}}
{%- endif -%}
{%- endmacro %}
### {{qualification.what}} 
{{ meta(qualification) }}
{{ abstract(qualification) }}
