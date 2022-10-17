from requests_html import AsyncHTMLSession
import openpyxl 
from bs4 import BeautifulSoup
import requests
import ast
import asyncio
import time
#########################################################################################################################################
################ EXCEL FILE: THIS FILE WILL PROVIDE THE SKUS THAT WILL BE SEARCHED, AND THEN THE PRICES FOUND WILL BE WRITTEN TO THIS FILE.
#########################################################################################################################################

# Filename="G:\\Boots Web Scraper\\BOOT PRODS.xlsx"

# ExcelFile = openpyxl.load_workbook("MHStar SKU.xlsx")
# ExcelSheet = ExcelFile.active

# mylist = []
# dict2 = {}

# for col in ExcelSheet['A']:
#      mylist.append(col.value)
#      dict2[col.value] = "N/A"

#asession  = AsyncHTMLSession()

urls1 = [
"https://www.boots.com/fragrance/perfume/all-perfume",
"https://www.boots.com/fragrance/aftershave/mens-aftershave"
]

######## Two URL groups are used to prevent overload on requests to the website

urls2 = [
"",
]

#########################################################################################################################################
################ THIS FUNCTION RUNS ASYNC AND WILL LOOP THROUGH EACH CATEGORY OF PRODUCTS UNTILL A MATCH IS FOUND (FROM SKUS LISTED IN EXCEL FILE)
################ WHEN A MATCH IS FOUND, THE SKU PRODUCT AND ITS PRICE ARE HELD IN A DICTIONARY TO BE LATER WRITTEN TO EXCEL
#########################################################################################################################################

def Scraper1(vurl):
    m = 0
    for x in range(0,100):
        url = vurl +"#facet:&productBeginIndex:%d&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:24&" % int(m)
        page = requests.get(url)
        print(url)
        time.sleep(2)
        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find_all(class_='product_name_link product_view_gtm')
        for x in name:
            tg = x['data-value']
            tg = tg.replace('.', '').replace(':false', ':False').replace(':true', ':True')
            tg = ast.literal_eval(tg)
            #print(tg)
            print(float(tg['price'])/100)
            print(tg['name'])
            print()

        #break
       # for x in products:
            # if x.attrs.get('sellersku') in mylist:
            #     print(x.attrs.get('sellersku'))
            #     price = float(x.attrs.get('price')) / 100
            #     print(price)
            #     dict2[x.attrs.get('sellersku')] = price
            #     print()

            #pass
            #print(x.text)
            # price = float(x.attrs.get('price')) / 100
            # print(price)
            # print()
        m += 24
for x in urls1:
    Scraper1(x)



#asession.run(*[lambda vurl=vurl: Scraper1(vurl) for vurl in urls1])
#asession.run(*[lambda vurl=vurl: Scraper1(vurl) for vurl in urls2])

#########################################################################################################################################
################ THIS FINAL PART WRITES ALL THE DATA FROM THE TEMP DICTIONARY, INTO THE EXCEL FILE FOR COMMERCIAL ANALYSIS
#########################################################################################################################################

# for x in dict2:
#     Row = mylist.index(x) + 1
#     ExcelSheet['B%d' % int(Row)] = dict2.get(x)

# ExcelSheet['B1'] = "Price"

#ExcelFile.save('MHStar SKU.xlsx')

