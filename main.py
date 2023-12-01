import requests
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# amazon_url = input("Please enter the Amazon link of the product you wish to buy: \n")

# print(Please get http header info from https://myhttpheader.com/)

# user_agent = input("What is the value of the User-Agent field?\n")
# accept_lang = input("What is the value of the Accept field?\n")
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0")
accept_lang = ("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
               "application/signed-exchange;v=b3;q=0.7")

headers = {
    "Request-Line": "GET / HTTP/1.1",
    "User-Agent": user_agent,
    "Accept": accept_lang
}

response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()
webpage = response.text
print(webpage)
