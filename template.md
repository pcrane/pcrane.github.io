{%- macro link_format(method) -%}{% if method.emoji %}{{ method.emoji }} {% endif %}[{{ method.value }}]({{ method.href }}){%- endmacro -%}

{%- include 'md/title.md' %}
{% if employment -%}
{%- include 'md/employment.md' -%}
{%- endif -%}
{%- if 0 -%}
{%- if projects -%}
{%- include 'md/projects-engineer.md' -%}
{%- endif -%}
{%- if projects -%}
{%- include 'md/projects-research.md' -%}
{%- endif -%}
{%- endif -%}
{%- if awards -%}
{%- include 'md/awards.md' -%}
{%- endif -%}
{%- if education -%}
{%- include 'md/education.md' -%}
{%- endif -%}
{%- if 0 -%}
{%- if memberships -%}
<h1>WARNING - FILL THE TEMPLATE FOR ASSOCIATION MEMBERSHIP</h1>
{%- endif -%}
{%- if research -%}
<h1>WARNING - FILL THE TEMPLATE FOR RESEARCH</h1>
{%- endif -%}
{%- if grants -%}
<h1>WARNING - FILL THE TEMPLATE FOR GRANTS</h1>
{%- endif -%}
{%- if invited -%}
<h1>WARNING - FILL THE TEMPLATE FOR INVITED TALKS</h1>
{%- endif -%}
{%- if consulting -%}
<h1>WARNING - FILL THE TEMPLATE FOR CONSULTING</h1>
{%- endif -%}
{%- if advisory -%}
<h1>WARNING - FILL THE TEMPLATE FOR ADVISORY BOARDS</h1>
{%- endif -%}
{%- endif -%}
{%- if publications -%}
{%- include 'md/publications.md' -%}
{%- endif -%}
{%- if service -%}
{%- include 'md/services.md' -%}
{%- endif -%}

