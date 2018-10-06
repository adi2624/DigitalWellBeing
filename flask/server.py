from flask import Flask
from flask import request
from flask import json
from flask import Response
import parser
app = Flask(__name__)

@app.route('/')
def api_root():
        return 'Welcome'


@app.route('/sendme', methods = ['POST'])
def api_articles():
    if request.headers['Content-Type'] == 'text/plain':
        article_data = parser.fetch_data(request.data)
        data={
            "link": request.data,
            "heading": article_data["heading"],
            "article": article_data["article_body"]
        }
        js = json.dumps(data)
        resp = Response(js,status=200,mimetype='application/json')
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


    