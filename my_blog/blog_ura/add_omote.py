import re
import os

os.chdir('ura')
ura_dirs = ['.', 'game', 'anime', 'comic', 'music']

for dir_ in ura_dirs:
    with open(os.path.join(dir_, 'index.html'), 'r', encoding='utf8') as f:
        f_html = f.read()
    with open(os.path.join(dir_, 'index.html'), 'w', encoding='utf8') as f:
        f.write(re.sub('omote/', '../', f_html))