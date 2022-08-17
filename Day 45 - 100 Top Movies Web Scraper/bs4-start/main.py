from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup)
# print(soup.prettify())
#
# returns FIRST tag of each kind
# print(soup.a)
# print(soup.li)
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# print(heading)
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)


# SCRAPE A LIVE WEBSITE --- news.ycombinator.com/news

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)
print(max_index)

print(article_texts[max_index])
print(article_links[max_index])



