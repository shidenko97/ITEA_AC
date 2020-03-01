from bs4 import BeautifulSoup

from funcs import simple_get

raw_html = simple_get("http://www.fabpedigree.com/james/mathmen.htm")
html = BeautifulSoup(raw_html, "html.parser")
for i, li in enumerate(html.select("li")):
    print(i, li)
