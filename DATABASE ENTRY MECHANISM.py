link='''<a href="https://www.amazon.in/HARPA-Synthetic-a-line-Dress-GR5759_Black_Large/dp/B07MMGN9GG/ref=as_li_ss_il?dchild=1&keywords=Harpa+Synthetic+a-line+Dress&qid=1581693255&sr=8-1&linkCode=li2&tag=multiversit0c-21&linkId=52379edfe9168c160b78bc7157d906db" target="_blank"><img border="0" src="//ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07MMGN9GG&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=multiversit0c-21" ></a><img src="https://ir-in.amazon-adsystem.com/e/ir?t=multiversit0c-21&l=li2&o=31&a=B07MMGN9GG" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'''
category='womens clothes'

def itemName(link):
	name="" ; count=0
	for i in link:
		if i == '/':
			count=count+1
		elif count >=3 and count <4:
			name=name+i
		else :
			pass
	return name
def pack(word):
	word=word.replace('"',"\\\'")
	return "\'" + word + "\',"
def packlast(link):
	link=link.replace('"',"\\\'")
	return "\'" + link + "\'"


name=itemName(link)
tableName='products'
# INSERT INTO 'products' (id, name, category, link) VALUES (NULL, '', '', 's')

sqlQuery= "\"INSERT INTO products (id, name, category, link) VALUES (NULL ," + pack(name) + pack(category) +packlast(link) + " )\" "
print("$sql = "+sqlQuery+";") 

# OUTPUT
'''$sql="INSERT INTO products (id, name, category, link) VALUES (NULL ,'HARPA-Synthetic-a-line-Dress-GR5759_Black_Large',
'womens clothes','<a href=\'https://www.amazon.in/HARPA-Synthetic-a-line-Dress-GR5759_Black_Large/dp/B07MMGN9GG/ref=
as_li_ss_il?dchild=1&keywords=Harpa+Synthetic+a-line+Dress&qid=1581693255&sr=8-1&linkCode=li2&tag=multiversit0c-21
&linkId=52379edfe9168c160b78bc7157d906db\' target=\'_blank\'><img border=\'0\' src=\'//ws-in.amazon-adsystem.com/widgets/q?
_encoding=UTF8&ASIN=B07MMGN9GG&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=
multiversit0c-21\' ></a><img src=\'https://ir-in.amazon-adsystem.com/e/ir?t=multiversit0c-21&l=li2&o=31&a=B07MMGN9GG
\' width=\'1\' height=\'1\' border=\'0\' alt=\'\' style=\'border:none !important; margin:0px !important;\' />' )" ;''' 


