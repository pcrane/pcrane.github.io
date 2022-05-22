{% extends 'md/section.md' %}

{% block section_title %}Teaching{% endblock %}

{% block section_body %}

### Lecturing ###
{#{% for class in lecturing %}#}
{% include 'md/lecturing.md' %}
{#{% endfor %}#}

### Demonstrating ###
{#{% for class in demonstrating %}#}
{% include 'md/demonstrating.md' %}
{#{% endfor %}#}

### Formal Feedback ###
{{ feedback.informal.preface }}

{% for comment in feedback.formal.comments %}
{% include 'md/feedback-formal.md' %}
{% endfor %}

### Informal Feedback ###
{{ feedback.informal.preface }}

{% for comment in feedback.informal.comments %}
{% include 'md/feedback-informal.md' %}
{% endfor %}
{% endblock %}