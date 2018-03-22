import requests
from bs4 import BeautifulSoup
#to parse main page
url = "https://niir.org/directory/"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
search_result=soup.find_all(class_="tbl-form")


ab=list()
ab1=list(list())
#to create list of all pages
for text in search_result:
    download = text.find_all('a')
for t in download:
    ab.append("https://niir.org"+t['href'])
#to parse and store the details of page
for q in ab:
    try:
        while(True):
            print(q)
            url1 = q
            page1 = requests.get(url1)
            soup1 = BeautifulSoup(page1.text, "html.parser")

            search_result1 = soup1.find_all("div", class_="d-con")
            for result in search_result1:

                name=result.find("h2").text
                desc=result.find("p").text
                add=result.find("address").text
                try:
                    inq=result.find("a",class_="d-eml")['href']
                except:
                    inq="not present"



                contacts=result.find("a",class_="d-vcf")['href']
                ab1.append([name,desc,add,inq,contacts])

            q="https://niir.org"+soup1.find("td",attrs={"class":"ts","valign":"top"}).find("a")['href']
        if(soup1.find("a",attrs={"title":"next"})):
            continue
        else:
            break

    except:
        continue






