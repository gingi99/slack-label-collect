from flask import Flask
import os
import json
import requests

app = Flask(__name__)

@app.route("/slack", methods=['POST'])
def hello():
    URL = 'https://hooks.slack.com/services/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'
    payload = {
        "text": "POSTがきたよ",
        "username": "Anomaly Response"
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(URL, data=json.dumps(payload), headers=headers)
    return 'OK'
    #data = json.load(request.data)
    #payload = {
    #    "response_type": "ephemeral",
    #    "text" : "message return"
    #} 
    #url = 'http://mattermost.dsl.nttv6.jp/hooks/rnrh3ywtoirs9y7ourxm3pk4sa'
    #headers = {'content-type': 'application/json'}
    #r = requests.post(url, data = json.dumps(payload) , headers = headers)
    #return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
