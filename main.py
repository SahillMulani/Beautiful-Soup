import requests
from bs4 import BeautifulSoup

url = "https://linktr.ee/offcampusplacement"

#Step 1 : Get the HTML
r = requests.get(url)
htmlContent= r.content
#print(htmlContent)

#Step 2 : Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#Step 3 : HTML Tree Traversal
# Types of Objects
'''
1. Tag
2. Navigable String
3. BeautifulSoup
4. Comment
'''
# Get the title of HTML Page
title = soup.title
#print(title)

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)


#Get first element in the HTML Page
# print(soup.find('p'))

#Get classes first element in the HTML Page
# print(soup.find('p')['class'])

#Get element with class lead in the HTML Page
# print(soup.find_all('p', class_='lead'))

#Get the text from the elements
# print(soup.find('p').get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
#print(anchor)

all_links = [ ]
# Get all the links from the Page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = link.get('href')
        all_links.append(linkText)

# Print all the links
for link in all_links :
    print(link + " ")