---
layout: article
titles:
  # @start locale config
  en      : &EN       Publications
show_title: false
permalink: /publications
---
<style>
  /* Remove bullets from the list */
  ul.publications-list {
    list-style: none;
    padding: 0;
  }

  /* Add margin and padding to each publication */
  ul.publications-list li {
    margin-bottom: 20px; /* Add space below each publication */
    padding: 10px; /* Add padding around each publication */
    border: 1px solid #ccc; /* Add border for visual separation */
    border-radius: 5px; /* Add rounded corners for aesthetics */
  }
</style>

<h2>Recent Publications</h2>

<ul class="publications-list">
  {% for publication in site.data.publications %}
    <li>
      <strong>{{ publication.title }}</strong><br>
      {{ publication.author }},
      <em>{{ publication.venue }}</em>,
      {{ publication.year }}<br>
      {% if publication.url %}
        <a href="{{ publication.url }}" target="_blank">Read more</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>
