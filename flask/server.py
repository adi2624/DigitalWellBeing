import os
from flask import Flask
from flask import request
from flask import json
from flask import Response
from flask import render_template
from flask_cors import CORS
import parser
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def api_root():
        return 'Welcome'

@app.route('/api',methods=['POST'])
def upload_image():
    file=request.files['image']
    f=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
    file.save(f)
    return render_template('image.html')
@app.route('/sendme', methods = ['POST'])
def api_articles():
    if request.headers['Content-Type'] == 'text/plain':
        string_url = str(request.data, 'utf-8')
        print(string_url)
        article_data = parser.fetch_data(str(string_url))
        data={
            "link": str(string_url),
            "heading": article_data["heading"],
            "article": article_data["article_body"]
        }
        js = json.dumps(data)
        resp = Response(js,status=200,mimetype='application/json')
        print("Sending back Response now")
        print(str(resp))
        return resp
    elif request.headers['Content-Type'] == 'application/json':
        print(json.dumps(request.json))
        json_object = json.loads(json.dumps(request.json))
        article_data = parser.fetch_data(json_object["link"])
        #print(json_object["id"])
        data={
            "link": json_object["link"],
            "heading": article_data["heading"],
            "article": article_data["article_body"]
        }
        js = json.dumps(data)
        resp = Response(js,status=200,mimetype='application/json')
        return resp

    else:
        return "415 Unsupported Media Type 😉"

app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + parser.fetch_data()

if __name__ == '__main__':
    app.run(host="0.0.0.0")


    