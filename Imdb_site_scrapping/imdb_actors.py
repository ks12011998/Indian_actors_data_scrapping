# -*- coding: utf-8 -*-
"""imdb_actors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujn0r6GVRUz2xsCTUY2GKVC4UdW_-4IF
"""

from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://www.imdb.com/list/ls025929404/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
lister_list = soup.findChildren('div', {"class" : 'lister-item mode-detail'})
print(lister_list)

print(lister_list[0])

import re
image = []
inn_div = lister_list[0].select('div > a')
image_tag = (inn_div[0].findChildren("img"))
print(image_tag[0]["alt"])
image.append((image_tag[0]["alt"],image_tag[0]["src"]))
print(image)

final_image_list = []
for i in range(len(lister_list)):
  image = []
  inn_div = lister_list[i].select('div > a')
  image_tag = (inn_div[0].findChildren("img"))
  # print(image_tag[0]["alt"])
  image.append((image_tag[0]["alt"],image_tag[0]["src"]))
  final_image_list.append(image)
print(final_image_list)

film= ""
inn_div = lister_list[0].select('p > a')
print(inn_div[0].text)

final_film_list= []
for i in range(len(lister_list)):
  inn_div = lister_list[i].select('p > a')
  # print(inn_div[0].text)
  final_film_list.append(inn_div[0].text)

print(final_film_list)

with open('film_list.txt','w') as fp:
  for i in range(len(final_film_list)):
    fp.write(final_film_list[i])
    fp.write('\n')

print(len(final_image_list))
print(len(final_film_list))

Personality_traits = []
inn_div  = lister_list[0].select('p')[1]
print(inn_div.text)

Final_personality_traits = []
for i in range(len(lister_list)):
  Personality_traits = []
  inn_div  = lister_list[i].select('p')[1]  
  print(inn_div.text)
  Personality_traits.append(inn_div.text)

  Final_personality_traits.append(Personality_traits)

print(Final_personality_traits)

with open('descriptions.txt', 'w') as fp:
  for i in range(len(Final_personality_traits)):
    fp.write(str(Final_personality_traits[i]))
    fp.write('\n')

for i in range(len(final_image_list)):
  if final_image_list[i] != "Photo not available": 
    print(final_image_list[i][0][0])
    response = requests.get(final_image_list[i][0][1],stream = True)
    print(response)
    file = open("/content/imdb_images/{}.jpg".format(final_image_list[i][0][0]), 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

!zip -r /content/images_file.zip /content/imdb_images

