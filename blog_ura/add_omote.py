import re
import os

os.chdir('ura')
ura_dirs = ['.', 'game', 'anime', 'comic', 'music']

for dir_ in ura_dirs:
    for f_name in os.listdir(dir_):
        if f_name[-5:] == '.html':
            with open(os.path.join(dir_, f_name), 'r', encoding='utf8') as f:
                f_html = f.read()
            with open(os.path.join(dir_, f_name), 'w', encoding='utf8') as f:
                f.write(re.sub('omote/', '../', f_html))