---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

The team that makes the dream work.

{% include section.html %}

{% include list.html
  data="members"
  component="portrait"
  filter="role == 'principal-investigator'"
%}

<div style="height: 2rem;"></div>

{% include list.html
  data="members"
  component="portrait"
  filter="role == 'postdoc'"
%}

{% include list.html
  data="members"
  component="portrait"
  filter="role == 'programmer'"
%}

<div style="height: 2rem;"></div>

{% include list.html
  data="members"
  component="portrait"
  filter="role == 'phd'"
%}

{% include list.html
  data="members"
  component="portrait"
  filter="role != 'principal-investigator' and role != 'postdoc' and role != 'phd' and role != 'programmer'"
%}

{% include section.html %}

## Team photos

{% include section.html %}

{% capture content %}

{% include figure.html image="images/Untitled Folder/IMG-20260522-WA0000.jpg" %}
{% include figure.html image="images/Untitled Folder/IMG-20260509-WA0000.jpg" %}
{% include figure.html image="images/Untitled Folder/20250929_170313.jpg" %}
{% include figure.html image="images/Untitled Folder/IMG-20260921-WA0005.jpg" %}
{% include figure.html image="images/Untitled Folder/20260505_153855.jpg" %}
{% include figure.html image="images/Untitled Folder/20260602_161523.jpg" %}
{% include figure.html image="images/Untitled Folder/20260628_131008.jpg" %}
{% include figure.html image="images/Untitled Folder/Snapchat-2108968296.jpg" %}

{% endcapture %}

{% include grid.html style="mosaic" content=content %}
