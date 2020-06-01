from bs4 import BeautifulSoup
import requests
import os

url = ("your link")

source = requests.get(url)
soup = BeautifulSoup(source.text,"html.parser")

link = []

para = soup.select('img[src^="https://slutmesh.com/wp-content/uploads"]')
print(para)

for img in para:
    link.append(img["src"])
for x in link:
    print(x)

os.mkdir("your directory")

i = 1

for index , img_link in enumerate(link):
    img_data = requests.get(img_link).content
    with open("your directory\\" + str(index+1)+".jpg", "wb+") as f:
        f.write(img_data)


