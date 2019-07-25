# AmazonMailer
Just another Amazon price scraper.
You can set a price, and if the product is cheaper than it, you recive a mail.

## Content Table
- [0. How it works](#How it works)
- [1. Usage](#Usage)
- [2. Credits](#Credits)

## How it works
The program take the amazon product url from the user. After, takes the product name and the price from the page by Requests. Then, ask the maximum price that the product must have. The program scans the amazon page hourly. When the product is less than your price, it sends you an email with smtplib.

## Usage
First of all, you must install all the requirements contained in required.txt file.
Then, you have to open the source and write:
1) The smtp server address at line 18 (default is the gmail ones)
2) The smtp post of the server at line 19
3) The smtp email address at line 20
4) The "reciver" mail at line 22
If you want, you can change the User Agent too at line 14-15

## Credits
This project is inspired by the video "Build A Python App That Tracks Amazon Prices" (https://youtu.be/Bg9r_yLk7VY). 
If you have suggestions or tips, PLEASE tell me: moiolijacopo4@gmail.com
