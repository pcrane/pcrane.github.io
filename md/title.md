# {% include 'md/name.md' %}

{% with role = employment|sort(attribute="when.start.year", reverse=true)|first %}{{ role.title }} at {{ role.employer }} {% endwith %}

{% if tag -%}
{{tag}}
{%- endif %}

{% for method in contact.methods %}
{%- include 'md/method.md' %}
{% endfor %}
