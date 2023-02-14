from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())


###############################################################################################
#               Finding and Selecting Particular Elements with BeautifulSoup
###############################################################################################


all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # tag_string = tag.getText()
    # print(tag_string)

    # tag_link = tag.get("href")
    # print(tag_link)
    pass

# heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)  # Books and Teaching
# print(section_heading.name)  # h3
# print(section_heading['class'])  # ['heading']

company_url = soup.select_one(selector="p a")  # selects anchor tag enclosed in a paragraph tag
print(company_url)

name = soup.select_one("#name")  # selects tag with id 'name'
print(name)

headings = soup.select(".heading")  # selects tag with class '.heading'
print(headings)

