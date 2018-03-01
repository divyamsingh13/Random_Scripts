import requests
from bs4 import BeautifulSoup
url = "https://www.fundoodata.com/companies-in/mumbai-navi-mumbai-l5"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
search_result1=soup.find_all(class_="search-result")
i=0
name1=list()
n=list()
normal1=list()
link=list()
i1=2
while(True):
    for table in search_result1:
        i=i+1
        try:
            name=table.find(class_="heading").text
            l=table.find("a").get("href")
            link.append("https://www.fundoodata.com/"+l)
            normal = table.find(class_="normal-detail").text
            normal1.append(normal)
            name1.append(name)




        except:
            continue
    try:
        url = "https://www.fundoodata.com/companies-in/mumbai-navi-mumbai-l5?&pageno="+str(i1)
        print("")
        i1=i1+1
        if(i1>10):
            break
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        search_result1 = soup.find_all(class_="search-result")
    except:
        print("end")
        break


print(name1)






