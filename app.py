import webbrowser,time,_thread
from flask import Flask,request,render_template


def web_view(port):
    webbrowser.open('http://127.0.0.1:'+str(port))

def run(port,app):
    app.run(port=port)

data = eval(open('config.json','r').read())

app = Flask(__name__)

#@app.route('/ckeditor/build/<file>')
#def aaaa(file):
#    return open('ckeditor/build/'+file,'r').read()

@app.route('/')
def index():
    return render_template('form.html')#open('form.html','r').read()

@app.route('/submit', methods=['POST'])
def submit():
    open('text.txt','w').write(request.form['html_text'])

@app.route('/check', methods=['POST'])
def check():
    text = "<html>\n<head>\n<meta charset=\"%s\">\n" % data['charset']
    text += request.form['head']
    text += "</head>\n"
    text += "<body {}>\n".format(request.form['body_attr'])
    text += request.form['scripts']
    text += request.form['body_tag']
    text += "</body>\n</html>"

    open('text.txt','w').write(text)
    return "sucess<br/>go to command line, complete and contenue"#'<html><body><form method="post" action="submit"><texterea name="html_text">{}</texterea><br><input type="submit" value="send"></form></body></html>'.format(text)

port = 8888

_thread.start_new_thread(run,(port,app))
time.sleep(1)
#threading.Thread(target=web_view,args=(port,))

web_view(port)
while True:
    pass
