{% extends 'md/section.md' %}

{% block section_title %}Publications{% endblock %}

{% block section_body -%}
{%- if 0 -%}
{%- with phd=publications.thesis.phd -%}
### PhD Thesis
- {% include 'md/phd.md' %}
{%- endwith -%}
{%- endif -%}
{%- with books=publications.books -%}
{%- if books -%}
### Books
{%- for book in books %}
- {% include 'md/book.md' -%}
{%- endfor -%}
{%- endif -%}
{%- endwith -%}
{%- with papers=publications.papers -%}
{%- if papers -%}
### Papers
{%- for paper in papers %}
- {% include 'md/paper.md' %}
{%- endfor -%}
{%- endif -%}
{%- endwith -%}
{%- with conferences=publications.conferences -%}
{%- if conferences -%}
### Conferences
{%- for conference in conferences %}
- {% include 'md/conference.md' -%}
{%- endfor -%}
{%- endif -%}
{%- endwith -%}
{%- with chapters=publications.chapters -%}
{%- if chapters -%}
### Book Chapters
{%- for chapter in chapters %}
- {% include 'md/chapters.md' -%}
{%- endfor -%}
{%- endif -%}
{%- endwith -%}
{%- with working=publications.working -%}
{%- if working -%}
### Working Papers
{%- for paper in working %}
- {% include 'md/working.md' -%}
{%- endfor -%}
{%- endif -%}
{%- endwith -%}
{% endblock %}