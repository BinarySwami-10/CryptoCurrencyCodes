import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import threading

#Recource Declaration
my_url = 'https://www.thehindu.com/sci-tech/technology/?page=1'
pageno=[]
l1=[]
l2=[]
l3=[]

#Page index generator
for i in range (0,216):
    string='https://www.thehindu.com/sci-tech/technology/?page='+str(i+1)
    pageno.append(string)



#gets page 1 to n and their contents
for j in range(0,5):
    #get soup in html format of current page index
    page_soup = soup(uReq(pageno[j]).read(),"html.parser")
    headings=page_soup.findAll("h3") 
    
    #Headings and relavant content Scanner for current page index
    for i in range (0,len(page_soup.findAll("h3"))):   
        try:
            #print(headings[i].a['title'])
            l1.append(headings[i].text)
            l2.append(headings[i].a['title'])
            l3.append(headings[i].a['href'])
        except:
            print("entry",i,'of page',j,'not found')
            
# \n correction  for list 1 to increase readability
lst1=[]
for i in range(len(l1)):
    #replace all \n with 'null'
	lst1.append(l1[i].replace("\n",""))
	#OPTIONAL:print(lst1[i])

#storing in JSON Usable Dictonary
allinfo={'titles':lst1,
         'date':l2,
         'links':l3}

#OPTIONAL
print(json.dumps(allinfo,indent=4))

with open('alldata.json','w') as f1:
    json.dump(allinfo,f1,indent=4)


