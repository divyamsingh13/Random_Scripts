import requests
from bs4 import BeautifulSoup
url = "https://www.fundoodata.com/companies-in/mumbai-navi-mumbai-l5"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
search_result1=soup.find_all("tbody")
print(len(search_result1))
i=0
name1=list()

norma1l=list(dict())
link=list()
for table in search_result1:
    i=i+1
    try:
        name=table.find(class_="heading").text
        name1.append(name)
        table1=table.find(class_="normal-detail")
        table1=table1.find("table")
        table1=table1.find("tbody")
        print(table1)

        rows=table1.findAll("tr")
        a=0
        for tr in rows:
            a=a+1
            print(tr)
            normal1[i][tr.find_all("td")[0]]=tr.find_all("td")[1]


    except:
        continue



    #print(table1)