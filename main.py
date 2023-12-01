import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

# Get the Amazon URL of the product the user wants to buy.
amazon_url = input("Please enter the Amazon link of the product you wish to buy: \n")
# amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Get the info from the user's http header information so the program can access the Amazon webpage.
print("Please get your http header info from https://myhttpheader.com/")

user_agent = input("What is the value of the User-Agent field?\n")
accept_lang = input("What is the value of the Accept field?\n")
# user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#               "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0")
# accept_lang = ("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
#                "application/signed-exchange;v=b3;q=0.7")

headers = {
    "Request-Line": "GET / HTTP/1.1",
    "User-Agent": user_agent,
    "Accept": accept_lang
}

# Access the Amazon webpage
response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()
webpage = response.text

# Get the price of the item.
soup = BeautifulSoup(webpage, "lxml")
whole_num = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
fraction_num = soup.find(name="span", class_="a-price-fraction").getText()

item_price = float(f"{whole_num}.{fraction_num}")

# Get the user's target price.
target_price = float(input("Please enter the maximum price you're willing to pay for the item: $"))

# Email the user if the item's price is less than the user's target price.
if item_price < target_price:
    sender = "dwdeathwolf@gmail.com"
    receiver = input("Please enter your email address: ")
    passkey = os.environ["PASS_KEY"]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=passkey)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject:Low Price!\n\nThe product you wish to buy is at ${item_price}, "
                f"lower than your target price of ${target_price}! Please buy it at {amazon_url}"
        )
