# required lib(s)
import requests
from os import system
from bs4 import BeautifulSoup
import time
import smtplib
# set the user agent that the program will use to access amazon (input yours instead of 'bla bla bla')
headers = {"User-Agent": 'bla bla bla'}
# smtp credential
#insert your data
smtp_server = 'smtp.google.com'    # google smtp server
smtp_port = 587    # google smtp port
smtp_addrs = ''   # smtp mail
smtp_passw = ''    # smtp password
your_email = ''    # reciver mail

# welcome things
def main():
    print("Welcome to AmazonMailer.py")
    print("This program send you an email if the price of an amazon product is less than you want")
    print("Let's go:")
    check_price()

def check_price():
    url = input("Input the amazon product url: ")
    # get the page
    page = requests.get(url, headers = headers)
    # read the content of the page
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    # search the value of title and price in the page
    title = soup2.find(id = "productTitle").get_text().strip()
    price = soup2.find(id = "priceblock_ourprice").get_text().strip()
    # converting the string into a float
    price=float(price[0:-5])
    print("The product '", title, "' costs ", price)
    # confirm
    save = input("Do you want to track the cost of this (y/n): ")
    if save == 'y' or save == 'Y':
        print("Item saved")
        # set the minimum price
        your_price = input("Type the price that you want: ")
        while True:
            if price < float(your_price):
                send_email()
                print("EMAIL SENDED")
                break
                system("EXIT")
            else:
                time.sleep(3600)
                continue
    else:
        print("Back to main menu")
        system("PAUSE")
        system("cls")
        main()

def send_email():
    server = smtplib.SMTP(smtp_server, smtp_port)

    #logging to server
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(smtp_addrs, smtp_passw)

    subject = "The product that you are tracking has reached your price!"
    body = ("Go to the app and SHOPPING!")
    message = f"Subject: {subject}\n\n{body}"

    # sent the email
    server.sendmail(
        smtp_addrs, # FROM
        your_email, # TO
        message # CONTENT
    )
    server.quit()

main()