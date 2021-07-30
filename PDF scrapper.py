import requests
from bs4 import BeautifulSoup
import smtplib

webs = []

# You will need to have installed the ChromeDriver to run this program properly
search_words = input('What do you want to search?').replace(' ', '+')

default_url = f"https://www.google.com/search?q={search_words}"

cookies = dict(CONSENT="YES+944")
source = requests.get(default_url, cookies=cookies)

soup = BeautifulSoup(source.text, 'html.parser')

list_of_pdfs = []
for link in soup.find_all('a'):
    webs.append(link.get("href"))

for j in webs:
    url = j.split('&')

    for i in url:
        if '.pdf' in i:
            list_of_pdfs.append(j.split('&sa=')[0])


def url_list():
    if len(list_of_pdfs) != 0:
        for u in list_of_pdfs:
            print(u.replace('/url?q=', ''))
        quit()
    else:
        print("No pdfs found")


# Sends you the list of the pdf if you want to look them later

print('Do you wish that we send you the link through your email?[yes, no]')
send_mail = input('> ')

if send_mail.lower() == 'yes':
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Replace this values
    email = "your@email.com"
    password = "your_Password123"

    # If you want to send yourself an email you will have to allow less secure apps in google using this link:
    # (https://www.google.com/settings/security/lesssecureapps)

    try:
        server.login(email, password)
        if send_mail:
            server.sendmail(email, email, list_of_pdfs)
            print("Hopefully you have send yourself an email with the list of pdfs")
            print("But this is the list of pdfs that we found:")
            url_list()

    except smtplib.SMTPAuthenticationError:
        print("Your username or password is incorrect, please write them again")
        print("Here are the pdf webs that we found:")
        url_list()
    quit()

else:
    print('These are the pdfs that we found: ')
    url_list()
