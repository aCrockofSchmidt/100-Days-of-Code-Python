import requests
from bs4 import BeautifulSoup
import smtplib
import os

TARGET_PRICE = 200

TARGET_URL = "https://www.amazon.ca/ShelterLogic-Shed-Box-Auger-Anchors/dp/B001G7Q230/?_encoding=UTF8&pd_rd_w=" \
             "rhffp&content-id=amzn1.sym.72b03f0f-4e11-4b99-b598-5b2869715532&pf_rd_p=72b03f0f-4e11-4b99-b598-" \
             "5b2869715532&pf_rd_r=BYY8R5PN7AMCB9B61DRN&pd_rd_wg=N1N0x&pd_rd_r=be4e55c8-a8b8-4a47-96ed-327b36605a8a&" \
             "ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1&psc=1"

HEADER = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/104.0.0.0 Safari/537.36",
    "Agent-Encoding": "gzip, deflate",
}

YAHOO_PASSWORD = os.environ.get("YAHOO_PASSWORD")

response = requests.get(url=TARGET_URL, headers=HEADER)
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
item_price = float(soup.find(name="span", class_="a-price-whole").getText())
#print(item_price)

if item_price < TARGET_PRICE:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user="the_legendary_flush@yahoo.com", password=YAHOO_PASSWORD)
        connection.sendmail(
            from_addr="the_legendary_flush@yahoo.com",
            to_addrs="the_legendary_flush@yahoo.com",
            msg=f"Subject: PRICE DROP NOTIFICATION!\n\nThe shed you want is below the target price on Amazon. Buy!"
        )

else:
    print("Item price remains above target. Do not buy today.")

