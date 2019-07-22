
# required lib(s)
import requests
from os import system
from bs4 import BeautifulSoup
import time
import smtplib
# set the user agent that the program will use to access amazon (input yours instead of 'bla bla bla')
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
# smtp credential
# insert your data
smtp_server = 'smtp.gmail.com'    # google smtp server
smtp_port = 587    # google smtp port
smtp_addrs = ''   # smtp mail
smtp_passw = ''    # smtp password
your_email = ''    # reciver mail

# welcome things
def main():
    system("cls")
    print("Welcome to AmazonMailer.py")
    print("This program send you an email if the price of an amazon product is less than you want")
    print("Let's go:")
    check_price()

def check_price():
    url = input("Input the amazon product url: ")
    try:
        # get the page
        page = requests.get(url, headers = headers)
        # read the content of the page
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
        # search the value of title and price in the page
        title = soup2.find(id = "productTitle").get_text().strip()
        price = soup2.find(id = "priceblock_ourprice").get_text().strip()
    except AttributeError:
        print("It seems that this link is not from amazon.")
        system("PAUSE")
        main()
    except requests.exceptions.MissingSchema:
        print("It seems that this link is not from amazon.")
        system("PAUSE")
        main()

    # converting the string into a float
    try:
        price=float(price[0:-5])
        print("The product '", title, "' costs ", price)
    except ValueError:
        print("Product with wrong price layout!")
        main()
    # confirm
    save = input("Do you want to track the cost of this (y/n): ")
    if save == 'y' or save == 'Y':
        print("Item saved")
        # set the minimum price
        your_price = input("Type the price that you want: ")
        while True:
            if price < float(your_price):
                send_email(title, url)
                print("EMAIL SENDED")
                break
                system("EXIT")
            else:
                print("MONITORING AMAZON...")
                time.sleep(3600)
                continue
    else:
        print("Your choice is wrong. Back to main menu")
        system("PAUSE")
        main()
    return url, title, price

def send_email(title, url):
    server = smtplib.SMTP(smtp_server, smtp_port)

    #logging to server
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(smtp_addrs, smtp_passw)

    subject = "The product '{}' that you are tracking has reached your price!".format(title)
    body = "Hi. \nThis is an automatic mail sended you by AmazonMailer. \nThe product that you war tracking as reached your price. check the link \n{}\nand BUY IT!".format(url)
    message = f"Subject: {subject}\n\n{body}"

    # sent the email
    server.sendmail(
        smtp_addrs, # FROM
        your_email, # TO
        message # CONTENT
    )
    server.quit()

main()