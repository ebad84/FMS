import requests

data = eval(open('config.json','r').read())

url = data["email_host_url"]#'http://api.cvstudy.ir/email_sender/'

sender = input('from email : ')
to = input('to email : ')
headers = "From: %s\nContent-type: text/html; charset=utf-8" % sender
subject = input('subject : ')
text = open(input('file text sending path : '),'r').read()

payload = {
    "email":to,
    "subject":subject,
    "sender":sender,
    "text":text,
    "headers":headers,
    }
out = requests.post(url,data=payload)
print(out.text)
