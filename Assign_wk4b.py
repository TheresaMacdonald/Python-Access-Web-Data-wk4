
#Using urllib in Python to read web pages and follow links at certain positions

import urllib
from BeautifulSoup import *


url = raw_input('Enter URL: ')
position = int(raw_input('Enter position: '))
line_count = int(raw_input('Enter count: '))


person_names = []


while line_count > 0:
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)
    tags = soup('a')
    person_name = tags[position-1].string
    person_names.append(person_name)
    url = tags[position-1]['href']
    line_count -= 1

print person_names[-1]


