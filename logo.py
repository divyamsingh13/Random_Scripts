import requests
from bs4 import BeautifulSoup
ans=[]
site = 'https://www.codechef.com/'
import pandas as pd


def modify_url(url):
    url=str(url)
    m_url = ''
    if url=="Not Mentioned":
        m_url="Not_Mentioned"
        return m_url
    url=url.split(".")

    for i in url:
        m_url=m_url+'.'+i
    return m_url[1:]


data=pd.read_csv('/home/divyam/PycharmProjects/mining/company .csv')
data.columns = ['id', 'name','website','contact','address','comp_city','comp_state','emp_size','revnue','industry','sub_industry']
urls=list(data['website'])
final_url=[]
for url in urls:
    url_modify=(modify_url(url))
    if 'www' in url_modify:
        final_url.append('https://'+url_modify)
f_url=[]
for i in final_url:
    if 'com' in i:
        index=i.index('com')
        i=i[:index+3]
        f_url.append(i)
    else:
        f_url.append(i)
ans=[]
for i in range(20):
    site=f_url[i]
    #print(site)
    try:
        response = requests.get(site)
    except:
        continue
    #print(response)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    for u in urls:
        #print(u)
        if 'logo' in u or "Logo" in u:
            if site not in u:
                ans.append(site+'/'+u)
            else:
                ans.append(u)
        break
print(ans)