from bs4 import BeautifulSoup as b
import requests
import time
import re

ref = re.compile("html?")
base = "https://ota.bodleian.ox.ac.uk"
def download_book(url,year,title):
    time.sleep(3)
    html = b(requests.get(base + url).text,'html.parser')
    #get the url of the html download file
    newurl=base + html.find("a",class_="filebutton label label-info",href=ref)["href"]
    #download the file
    time.sleep(3)
    file = requests.get(newurl).content
    #write it to a local file for later use.
    with open(f'{year}0/{title}.txt','wb+') as outfile:
        outfile.write(file)
    return

def find_books(url):
    time.sleep(3)
    #return the url of the next search page, if applicable
    soup = b(requests.get(url).text,"html.parser")
    #check to make sure the book is Publicly Available
    for jj in soup.find_all("li",class_="item-box"):
        if jj.find("div",class_="item-label PUB").span.string!="Publicly Available":
            pass
        year = str(jj.find("span",class_="date").string)[:3] #we just care about the decade
        #grab all the books urls
        book = jj.find("div",class_="artifact-title")
        url = book.a.get("href")
        #grab the publication year and title
        title = book.a.string.split(".")[0].replace('/','').split(',')[0]
        title = title[:min(len(title),25)]
        download_book(url,year,title)
    #if nexturl doesn't exist:
    nextthing = soup.find("li", class_="next")
    #print(nextthing)
    if nextthing == None:
       return None
    return base+nextthing.a["href"]

first = "https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/5/recent-submissions?"
print("got here")
i =1
while first != None:
    print(f"loop {i} out of {25368//5 + 1}")
    first = find_books(first)
    i+=1