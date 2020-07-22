cd blog
mkdocs.exe build -q
cd ../blog_ura
mkdocs.exe build -q
python add_omote.py
mv ura ../blog/site
cp -r ../blog/site/* ../Chokie-Zhang.github.io
rm -r ../blog/site