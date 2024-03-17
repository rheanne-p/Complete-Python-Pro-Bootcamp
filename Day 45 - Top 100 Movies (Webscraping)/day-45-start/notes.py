from bs4 import BeautifulSoup
# import lxml ("lxml" instead of "html.parser")

# OPEN HTML FILE
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# SOUP OBJECT
soup = BeautifulSoup(contents, "html.parser")

# SOUP ATTRIBUTES     name          string
print(soup.title)  # <title>Angela's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)  # Angela's Personal Site

# SOUP METHODS
print(soup.prettify())  # formats String with indents

# OBTAIN FlIRST COMPONENT
print(soup.a)  # first anchor tag

# OBTAIN ALL COMPONENTS: find_all() method
all_anchor_tags = soup.find_al(name="a")  # finds all anchor tags (list)

for tag in all_anchor_tags:

    tag_content = tag.getText()  # gets text within anchor tags
    print(tag_content)

    tag_href = tag.get("href")  # gets element specified in (): hrefs
    print(tag_href)

# ISOLATING BY ID
heading = soup.find(name="h1", id="name")  # specify tag name, id
print(heading)

# ISOLATING BY CLASS
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# OBTAINING CLASS
class_of_section_heading = section_heading.get("class")
print(class_of_section_heading)

# SPECIFIC ANCHOR TAG: p, em, strong, a
company_url = soup.select_one(selector="p em strong a")  # narrow down using steps
print(company_url)

soup.select(selector="#name")  # select by id name

soup.select(selector=".heading")  # select by class heading (returns a list)