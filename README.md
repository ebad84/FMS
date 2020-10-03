# FMS

Fake mail Sender. its for fun or hack??

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
git clone https://github.com/ebad84/FMS.git
pip3 install requierments.txt
```

## running

if you wanna to use YOUR template, just run the sender.py

```bash
python3 sender.py
```

but if you wanna to CREATE YOUR template, first run the app.py then run the sender.py

```bash
python3 app.py
venv\Scripts\python.exe app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8888/ (Press CTRL+C to quit)
127.0.0.1 - - [03/Oct/2020 22:01:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2020 22:01:12] "GET /styles.css HTTP/1.1" 404 -
Traceback (most recent call last):
  File "app.py", line 48, in <module>
    pass
KeyboardInterrupt

python3 sender.py
from email : test@telegram.com
to email : ***********@gmail.com
subject : 1st of hacker!!
file text sending path : text.txt
sucess
```

## Contribution
this program is open source and created for *learnin*. do not use it for hacking or etc.


Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)