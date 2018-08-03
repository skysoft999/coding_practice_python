#Coder: Sanu k yadav


from bs4 import BeautifulSoup
import requests
import os, os.path, csv
import threading

listingurl = 'https://grofers.com/cn/household-needs/laundry-detergents/cid/18/983'
response = requests.get(listingurl)
soup_html = BeautifulSoup(response.text, "html.parser")
# print(soup_html.body)
containers = soup_html.findAll("div", {"class" : "plp-product"})
# print(len(containers))
filename = "grofers_groc.csv"
f = open(filename,"w")
headers = "Product_name,Quantity,Current_price,Original_price\n"
f.write(headers)

for i in containers:
    try:
        if i.find("div", class_="plp-product__price--old display--inline-block@mobile"):
            old_price = i.find("div", class_="plp-product__price--old display--inline-block@mobile").get_text()
        else: 
            old_price = "-"
        name = i.find("div", class_="plp-product__name").get_text()
        quant = i.find("div", class_="plp-product__quantity").get_text()  
        new_price = i.find("span", class_="plp-product__price--new").get_text() 
        data1 = name + "," + quant + "," + new_price + "," + old_price + "\n"
        f.write(data1)
    except Exception as e:
        print(e)   
f.close()       
    
