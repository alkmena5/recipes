import os
from urllib.parse import quote
from shutil import copy

DIRECTORIES = {
   'vdohnovenie': 'Вдохновение',
   'vebinary': 'Вебинары',
   'na_kazdiy_den': 'На каждый день',
   'recepti': 'Рецепты',
   'teoria': 'Теория',
}

counter = 1

html: str = '<html><head>' + \
'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">' +\
'<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>' +\
'</head><body><ul>'

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.lower().endswith('.html') and root.count('/') <= 1:
        href: str = os.path.join(root, name)
        dst = os.path.join(root, f'file_{counter}.html')
        counter += 1
        copy(os.path.join(root, name), dst)
        encoded = f'https://github.com/alkmena5/recipes/blob/main/{quote(dst[2:])}'
        html += f'<li><a href="https://htmlpreview.github.io/?{encoded}">{root} --- {name}</a></li>'
html += f'</ul></body></html>'

with open('index.html', 'w') as f:
   f.write(html)


