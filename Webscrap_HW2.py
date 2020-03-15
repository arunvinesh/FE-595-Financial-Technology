import urllib.request
from bs4 import BeautifulSoup

#f = open("output_Webscrap_HW2.txt", "w")

url = "http://18.207.92.139:8000/random_company"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page)

soup.unicode

table1 = soup.find("table", border=1)
table2 = soup.find("body")
table3 = soup.find_all("ol")

for td in table3:
    rn = soup.find_all("li")[0].get_text()
    sr = soup.find_all("li")[1].get_text()
    d = soup.find_all("li")[2].get_text()
    n = soup.find_all("li")[3].get_text()
    p = soup.find_all("li")[4].get_text()

    #print(rn + "," + p+ ",", file=f)
    print(rn + "," + p )
