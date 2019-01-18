import requests
from bs4 import BeautifulSoup
from PIL import Image

url_link = input('Enter the Url:')
r = requests.get(url_link)

soup_obj = BeautifulSoup(r.text,"lxml")
links = soup_obj.findAll('img')

i = 1

for link in links:
    try:
        src=link['src']
        print(src)
        response = requests.get(src,stream=True)
        img=Image.open(response.raw)
        for j in range(0,10):
            img.save('/Users/srimanikanta/Desktop/Image-Scrapper/Images/image{}.jpg'.format(i))
            #cv.SaveImage('pic{:>05}.jpg'.format(i), j)
    except:
        print(KeyError)
    i += 1

