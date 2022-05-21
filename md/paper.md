{%- macro present(author) -%}
{{author.initial}}. {{author.lastname}}
{%- endmacro -%}

{%- macro highlight(author) -%}
{%- if author.format -%}
**{{present(author)}}**
{%- else -%}
{{present(author)}}
{%- endif -%}
{%- endmacro -%}

{%- macro to_list(iterable) -%}
{%- for iter in iterable -%}{{ highlight(iter) }}, {% endfor -%}
{%- endmacro -%}

{{ to_list(paper.authors) }}{{ link_format(paper.paper.href, paper.title, paper.paper.onclick) }}, _{{ paper.booktitle }}_ {{ paper.year }}, {{ paper.where }}.