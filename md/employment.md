{% extends 'md/section.md' %}

{% macro date_range(when) %}
{{ when.start.month }} {{ when.start.year }} -
{%- if when.end %} {{ when.end.month }} {{ when.end.year }}{% else %} present{% endif %}
{% endmacro %}

{% macro to_list(iterable) %}
{%- for iter in iterable -%}
* {{ iter }}
{% endfor -%}
{%- endmacro -%}

{% macro job_title(job) %}
### {{ job.title }}
{% if job.employer %}{{ job.employer }}{% endif -%}
{{ date_range(job.when) }}
{{ job.outline }}
{%- endmacro %}

{% macro job_responsibilities(job) %}
#### Responsibilities

{{ to_list(job.responsibilities) }}
{%- endmacro %}

{% macro job_achievements(job) %}
#### Achievements
{% if job.achievements.note %}
{{ job.achievements.note }}
{% else %}{% endif %}
{{ to_list(job.achievements.list) }}
{%- endmacro %}

{% block section_title %}Employment{% endblock %}
{% block section_body -%}
{%- for job in employment | sort(attribute="when.start.year", reverse=true) if job.visible -%}
{{ job_title(job) }}
{%  if job.achievements or job.responsibilities -%}
{%- if job.responsibilities -%}
{{ job_responsibilities(job) }}
{%- endif -%}
{%- if job.achievements -%}
{{ job_achievements(job) }}
{%- endif -%}
{%- else %}
{% endif %}
{%- endfor %}
{% endblock %}