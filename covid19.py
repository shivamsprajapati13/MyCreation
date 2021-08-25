import COVID19Py
from pynotifier import Notification
covid19=COVID19Py.COVID19(data_source="jhu")
latest=covid19.getLatest()
string = "Confirmed :"+str(+latest["confirmed"])+"\nRecovered :"+str(latest["recovered"])+"\nDeaths :"+str(latest["deaths"])
Notification(title="Today COVID19 News updates.",description=string,duration=10,).send()







# import requests
# from bs4 import BeautifulSoup
# import time
# import webbrowser

# def find_price(URL):
#     r = requests.get(URL,headers={"User-Agent":"Defined"})
#     soup = BeautifulSoup(r.content,"html.parser")
#     try:
#         if 'amazon' in URL:
#             try:
#                 price_one = soup.find(id="priceblock_dealprice")
#                 price = price_one
#             except:
#                 price = price_two
#                 price_two = soup.find(id = "priceblock_ourprice")
#             return price
#         elif 'flipkart' in URL:
#             price = soup.find(class_ = '_1vC4OE _3qQ9m1')
#             return price
#     except:
#         return
# i =1 
# URL = input(" Enter the url:: ")
# while True:
#     price = find_price(URL)
#     if price == None:
#         print("Invalid link")
#         break
#     else:
#         if (i<2):
#             current_price = price.get_text()
#         previous_price = current_price
        
#         print(f"Your current price is :: {price.get_text()}")
        
#         if i>2:
#             current_price = price.get_text()
#             if current_price!= previous_price:
#                 webbrowser.open_new(URL)

#         time.sleep(10)

