# -*- coding: utf-8 -*-
"""Wiki_actors

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yWSssIlA__K2gdVh3VsDyI499I0w_FF6
"""

from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://en.wikipedia.org/wiki/List_of_Indian_film_actors/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
mw_div = soup.findChildren('div', {"class" : 'mw-body-content'})

# print(mw_div)

mw_content = soup.select('div')
mw_div = mw_content[2]
mw_body = mw_div.select('div')
mw_content_ldr = mw_body[2]
print(mw_content_ldr.select('div'))
all_div_in = []
for div in mw_content_ldr:
    if div:
      all_div_in.append(div)
# print(all_div_in)

print(aas)

url = "https://en.wikipedia.org/wiki/A._K._Hangal/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
div_cont = soup.find_all('a', class_='image')
print(div_cont)

url = "https://en.wikipedia.org/wiki/List_of_Indian_film_actors/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
links = soup.find_all('a',class_='div-col columns column-width')
li = []
for link in links:
    url = link.get("href", "")
    if "/wiki" in url:
      li.append(url)      
print(li)

import requests
import lxml.html as lh
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_Indian_film_actors'#Create a handle, page, to handle the contents of the website
page = requests.get(url)#Store the contents of the website under doc
doc = lh.fromstring(page.content)#Parse data that are stored between <tr>..</tr> of HTML
ul_elements = doc.xpath('//li')
print(ul_elements)

url = "https://en.wikipedia.org/wiki/List_of_Indian_film_actors"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
li = soup.select("#content #bodyContent #mw-content-text  ul > li  > a")
final_links = []
for link in li:
    # print(link.get('href'))
    final_links.append(link.get('href'))
print(final_links[26:])

for i in range(len(final_links[:50])):
  url = "https://en.wikipedia.org" + str(final_links[i])
  # print(url)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  mw_div = soup.findChildren('table', {"class" : 'infobox biography vcard'})
  # mw_div = soup.select('')
  li1 = soup.find('table', {'class': 'infobox biography vcard'}) 
  #li2 = soup.find("table", {"class": "infobox biography vcard"}).select("tbody > tr")
  li = soup.select("#content #bodyContent #mw-content-text .mw-parser-output .infobox biography vcard table > tbody  > tr")

final_data = []
final_links = final_links[26:]
# print(final_links)
for i in range(150):
  url = "https://en.wikipedia.org" + str(final_links[i])
  # print(url)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  My_table = soup.find('table',{'class':'infobox biography vcard'})
  # print(My_table)
  final_data.append(My_table)

print(final_data)

print(final_data[2])

name= ""
image_list = []
born = ""
years_active = []
for i in range(len(final_data)):
  if final_data[i]:
    image_cont = final_data[i].select("tbody > tr  > td > a > img")
    if image_cont:  
      image_list.append(image_cont[0]['src'])
    else:
      image_list.append(None)
      
print(image_list)

born_list = []
for i in range(len(final_data)):
  if final_data[i]:
    born_ = final_data[i].select("tbody > tr  > td > span")
    if born_:
      born = born_[0].text
      born_list.append(born)  
    else:
      born_list.append("No data found")

print(born_list)
print(len(born_list))

with open('born_list.txt','w') as fp:
  for b in born_list:
    fp.write(b)
    fp.write('\n')

Years_active_list = []
import re
pattern = re.compile("")
for i in range(len(final_data)):
  years_active = []
  if final_data[i]:
    main = final_data[i].select("tbody > tr ")
    if main:
      li = []
      for i in range(len(main)):
        res = (main[i].select("td"))
        for val in res:
          if pattern.match(val.text):
            print(val.text)
          # if re.compile('^\d{4}$-\d{4}$'):
          #   print(res)

  Years_active_list.append(years_active)

print(Years_active_list)

final_occupation_list = []
for i in range(len(final_data)):
  if final_data[i]:
    occupation_1 = []
    occ = final_data[i].select("tbody > tr > td")
    print(occ)
    #   occ_inn =occ[3]
    #   for val in occ_inn_1:
    #     occupation_1.append(val.text)
    # else:
    #   occupation_1.append("Data not found")
  final_occupation_list.append(occupation_1)

print(final_occupation_list)

final_name_list= []
final_image_list = []
final_born_list = []
final_active_list = []
final_occupation_list = []

name_list = []
for i in range(len(final_data)):
  if final_data[i]:
    name_div =  final_data[i].select("tbody > tr  > th > div")
    # print(name_div)
    for value in name_div:
      name = (value.text)
      name_list.append(name)
name_list = (name_list)

name_list.remove('Works')
print(name_list)

print(name_list)
print(len(name_list))
with open('name_list.txt', 'w') as fp:
  for name in name_list:
    fp.write(name)
    fp.write('\n')

image_list = []
count=0
for i in range(len(final_data)):
  if final_data[i]:
    image_cont = final_data[i].select("tbody > tr  > td > a > img")
    if image_cont :  
      image_list.append(image_cont[0]['src'])
      
    else:
      image_list.append("Photo not available")
      count+=1
      
     
print(len(image_list))

print(image_list)
with open('image_list.txt','w') as fp:
  for image in image_list:
    fp.write(image)
    fp.write('\n')

div_cont = final_data[0].find('div', class_='toc')
print(div_cont)

All_reference_links = []
for i in range(len(final_data)):
  temp = []
  url = "https://en.wikipedia.org" + str(final_links[i])
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  mw_div = soup.findChildren('div', {"class" : 'toc'})
  if mw_div:
    li = mw_div[0].select("ul > li > a")   
    if li:
      for link in li:
        # print(link.get('href'))
        temp.append(link.get('href'))
    else:
      temp.append("Data not found")
      
  All_reference_links.append(temp)

print(All_reference_links)
with open('reference_links','w') as fp:
  for li in All_reference_links:
    fp.write(str(li))
    fp.write('\n')

def download_image(image):
    response = requests.get(image[0], stream=True)
    file = open("/content/images/{}.jpg".format(realname), 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

for i in range(len(image_list)):
  print(image_list[i])

for i in range(len(temp_list)):
  temp_list[i] = str(temp_list[i])

idx = 1
from PIL import Image
image = Image.new('RGB', (300, 300))
for i in range(len(image_list)):
  if image_list[i] != "Photo not available": 
    print("http:" + image_list[i])
    response = requests.get("http:" + temp_list[i][0:],stream = True)
    print(response)
    file = open("/content/images/{}.jpg".format(idx), 'wb')
    response.raw.decode_content = True
    idx+=1
    shutil.copyfileobj(response.raw, file)
    del response
  else:
    image.save('/content/images/empty.jpg')
    idx+=1

!zip -r /content/file.zip /content/images

from google.colab import files
files.download("/content/file.zip")