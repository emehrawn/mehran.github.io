html_doc =""" 
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc , "html5lib")
"""for link in soup.find_all('a'):            #prints out all the links in tag a
    print(link.get('href'))"""

soup.title                                          #if we print it
# <title>The Dormouse's story</title>

soup.title.name                                     #if we print it
# u'title'

soup.title.string                                   #if we print it
# u'The Dormouse's story'

soup.title.parent.name                              #if we print it
# u'head'

soup.p                                              #if we print it, if we'd typed Soup.find_all('p') it would've printed all p tags, and same apply to others
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']                                      #if we print it
# u'title'

soup.a                                               #if we print it
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')                                   #if we print it
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")                                 #if we print it
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>        